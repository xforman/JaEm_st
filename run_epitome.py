from typing import List

import numpy as np
import torch
import wandb
wandb.init(mode="disabled")

import argparse
import pprint
import pandas as pd
np.seterr(all='raise')


def calc_metrics(pth, output_dir_base, metrics: List[str], run_pref: str = "",
                 save_epi: bool = False):
    test_df = pd.read_csv(pth, sep="~")
    test_df = test_df[test_df['gens'].str.len() != 0]
    res = {}
    if "epitome" in metrics:     # Calculate EPITOME, DIFF-EPITOME metrics
        from diff_epitome import EmpathyScorer, to_epi_format, get_epitome
        opt = {'no_cuda': False}
        device = 0
        opt['epitome_save_dir'] = "checkpoints/epitome_checkpoint"
        epitome_empathy_scorer = EmpathyScorer(opt, batch_size=1,
                                               cuda_device=device)
        epi_in = to_epi_format(test_df["prevs"].to_list(),
                               test_df["gens"].to_list(),
                               test_df["gens"].to_list())

        _, pred_IP_scores, pred_EX_scores, pred_ER_scores = get_epitome(
                epi_in, epitome_empathy_scorer)

        if save_epi:
            test_df["pred_IP_scores"] = pred_IP_scores
            test_df["pred_EX_scores"] = pred_EX_scores
            test_df["pred_ER_scores"] = pred_ER_scores
            new_pth = pth.replace(".csv", "_epi.csv")
            test_df.to_csv(new_pth, sep="~")

        # epitome_report = avg_epitome_score(
        #         pred_IP_scores, pred_EX_scores, pred_ER_scores, gt_IP_scores,
        #         gt_EX_scores, gt_ER_scores, diff_IP_scores, diff_EX_scores,
        #         diff_ER_scores)

        # res["epitome"] = {k: str(v) for k, v in epitome_report.items()}
        # wandb.log({run_pref + "_" + "diff_er": res["epitome"]["diff_ER"]})
        # wandb.log({run_pref + "_" + "diff_ex": res["epitome"]["diff_EX"]})
        # wandb.log({run_pref + "_" + "diff_ip": res["epitome"]["diff_IP"]})
        del epitome_empathy_scorer

    # if "bertscore" in metrics:
    #     from evaluate import load
    #     bertscore = load("bertscore")

    #     preds = test_df["gens"].to_list()
    #     refs = test_df["gen_targets"].to_list()

    #     bs_results = bertscore.compute(predictions=preds,
    #                                    references=refs, lang="en")
    #     pbert = np.mean(bs_results["precision"])
    #     rbert = np.mean(bs_results["recall"])
    #     f1bert = np.mean(bs_results["f1"])
    #     # wandb.log({run_pref + "_" + "bertf1": f1bert})

    #     res["bertscore"] = {"p_bert": str(pbert), "r_bert": str(rbert),
    #                         "f1_bert": str(f1bert)}

    # Write results
    # bert_pth = pth.replace("preds", "epib")
    # with open(bert_pth, 'w') as f:
    #     f.write(
    #         pprint.pformat(res, compact=True).replace("'", '"'))
    #     print(f"4.-----Saving df metrics (SFT) to: {bert_pth}--------")


def main(args: argparse.Namespace) -> None:
    output_dir_base = args.base_dir
    pth_to_csv = f"{output_dir_base}/{args.df_name}"
    calc_metrics(pth_to_csv, output_dir_base, ["epitome"], save_epi=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--df_name", help="file name of the dataframe")
    # parser.add_argument("-s", "--save_epi", default=False,
    #                     help="save epitome scores per line",
    #                     action=argparse.BooleanOptionalAction)
    # parser.add_argument("-m", "--metrics", nargs="+",
    #                     help="one or more of: epitome, bertscore")
    parser.add_argument("-d", "--base_dir", default="./results",
                        help="base dir with saved models")

    main(parser.parse_args())

