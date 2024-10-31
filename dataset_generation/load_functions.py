import re
import os
import json


def load_samples(metadata):
    samples_path = metadata["eval_sample_dir"]
    sample_dims = metadata["sample_dims"]
    raw_samples = [x for x in os.walk(samples_path)]
    cleaned_files = []
    for x in raw_samples[0][2]:
        with open(samples_path + '/' + x, 'r') as f:
            print(x)
            raw_file = f.read()
            clean_file = re.sub(r'Answers|Conversation', 'Context', raw_file).split("Context:")
            cleaned_files.append(clean_file)

    return cleaned_files


def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    f.close()
    return data