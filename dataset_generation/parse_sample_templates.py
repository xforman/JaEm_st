import re
import pandas as pd
import numpy as np


def split_answers(answers, answer_dims):
    answers = answers.replace("\n", "")
    dims = [dim + ": " for dim in answer_dims]
    dim_indices = np.array([answers.index(dim) for dim in dims])
    
    for i in range(len(dim_indices)):
        dim_indices[np.argmax(dim_indices)] = len(dim_indices) - i

    answers = re.sub("|".join(dims), "\n", answers).split("\n")[1:]
    labeled_answers = [(dims[dim_indices[i]].replace(": ", ""), answers[i])
                       for i in range(len(dim_indices))]
    return labeled_answers


def parse_samples(samples, prompts, sample_dims, answer_dims):
    sample_templates = pd.DataFrame(samples, columns=sample_dims)
    sample_templates['sample_index'] = sample_templates.index

    # split the conversation into turns
    sample_templates['Conversation_split'] = sample_templates["Conversation"].str.replace("Jane:", "Carl:").str.split("Carl:")
    
    #sample_templates['Previous_utterance'] = sample_templates["Conversation_split"].apply(lambda x: x[-2])
    sample_templates["Answers_split"] = sample_templates["Answers"].apply(split_answers, 
                                                                         answer_dims=answer_dims)

    # add prompts
    sample_templates["CE_prompt"] = prompts["CE"][0]
    sample_templates["AE_prompt"] = prompts["AE"][0]
    sample_templates["ERA_prompt"] = prompts["ERA"][0]
    return sample_templates


    

    

