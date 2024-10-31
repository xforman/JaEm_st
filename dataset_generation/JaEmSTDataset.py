from torch.utils.data import Dataset
import torch

class JaEmST(Dataset):
    def __init__(self,
                 sample_indices,
                 templates,
                 em_dim,
                 input_template,
                 randomized_answers=None
                 ):

        self.samples_context = sample_indices     # dataframe of all samples
        self.templates = templates
        self.em_dim = em_dim
        self.input_template = input_template
        self.shuffled = randomized_answers

    
    def __len__(self):
        return len(self.samples_context)
    
    def __getitem__(self, index):
        # get sample atributes
        sample_context = self.samples_context.iloc[index]
        shuffled_answers = self.shuffled.iloc[index] if self.shuffled is not None else None
        
        template = self.templates.iloc[sample_context['sample_index']]
        filled_template, shuffled = self.em_dim(template, sample_context, 
                                                shuffled_answers)
        return filled_template, shuffled