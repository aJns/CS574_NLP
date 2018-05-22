# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:14:31 2018

"""
from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


def read_txt(filepath):
    x = []
    with open(filepath,'r') as f:
        content = f.read()
        oneline = content.replace("\n"," ")
        depunc = strip_punctuation(oneline)
        x.append(depunc.split())
    return x


data_dir = "../project-data/Adventures of Huckleberry Finn/"
ref_paths = [
        "gradesaver_huckfinn.txt"
        ,"cliffsnotes_huckfinn.txt"
        ,"wiki_huckfinn.txt"
        ]
summary_path = "sparknotes_huckfinn.txt"

refs = []
for r_path in ref_paths:
    refs.append(read_txt(data_dir+r_path)[0])
ref_list = [refs]
sum_list = read_txt(data_dir+summary_path)


from nltk.translate.bleu_score import corpus_bleu
score1 = corpus_bleu(ref_list, sum_list, weights=(1,0, 0, 0))
score2 = corpus_bleu(ref_list, sum_list, weights=(0,1, 0, 0))
print(score1)
print(score2)