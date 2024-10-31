import pandas as pd
import numpy as np


def create_affective_st(sample, bias_dims_single, extra=None):
    bds = bias_dims_single
    template = sample["AE_prompt"] + sample["Context"] + sample["Conversation"]
    filled_template = template.format(GENDER=bds['gender'], PRONOUN=bds["pronoun"], AGE=bds["age"], RACE=bds["race"],
                         SOCECON=bds["socio-economic status"], EDUCATION=bds["education"], RELIGION=bds["religion"])
    return filled_template, []


def create_cognitive_st(sample, bias_dims_single, shuffled=None):
    bds = bias_dims_single
    answers = sample["Answers_split"]
    if shuffled is None:
        shuffled = np.random.choice(np.arange(len(answers)), len(answers), replace=False)

    formatted_answers = ["\n" + chr(65 + i) + ": " + answers[answer][1] for i, answer in enumerate(shuffled)]
    formatted_answers = "\n".join(formatted_answers)
    
    template = sample["CE_prompt"] + sample["Context"] + sample["Conversation"] + formatted_answers
    filled_template = template.format(GENDER=bds['gender'], PRONOUN=bds["pronoun"], AGE=bds["age"], RACE=bds["race"],
                         SOCECON=bds["socio-economic status"], EDUCATION=bds["education"], RELIGION=bds["religion"])
    return filled_template, shuffled