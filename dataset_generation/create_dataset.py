import json

from load_functions import load_json, load_samples
from parse_sample_templates import parse_samples
from combine_social_dims import combine_social_dims


# load and parse sample templates
def load_sample_templates(metadata):
    samples = load_samples(metadata)
    prompts = load_json(metadata["prompts_source"]) 
    sample_dims = metadata["sample_dims"]
    answer_dims = metadata["answer_dims"]
    return parse_samples(samples, prompts, sample_dims, answer_dims)


# create combinations of social dimensions
def create_bias_context(metadata, n_samples):
    social_group_vals = load_json(metadata["bias_dims_source"])
    social_groups = metadata["social_groups"]
    to_eval = [social_groups[i] for i in metadata["evaluated_dims"]]
    return combine_social_dims(to_eval, social_groups, 
                               social_group_vals, 
                               n_samples,
                               metadata["dataset_size"])


def create_dataset(metadata_path="dataset_metadata.json"):
    metadata = load_json(metadata_path)
    sample_templates = load_sample_templates(metadata)
    bias_context = create_bias_context(metadata, sample_templates.shape[0])
    
    return bias_context, sample_templates
