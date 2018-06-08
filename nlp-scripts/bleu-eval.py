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

#not fahrenheit, emma, belljar(encoding), grapes, hobbit (encoding)
book = "huckfinn"
ref_dir = "../project-data/Adventures_of_Huckleberry_Finn/"
ref_paths = [
        "gradesaver_" + book + ".txt"
        ,"sparknotes_" + book + ".txt"
        ,"cliffsnotes_" + book + ".txt"
        ,"wiki_" + book + ".txt"
        ]
summary_path = "summary_Mark_Twain_the_Adventures_of_Huckleberry_Finn.txt"

refs = []
for r_path in ref_paths:
    refs.append(read_txt(ref_dir+r_path)[0])
ref_list = [refs]
sum_list = read_txt(summary_path)


from nltk.translate.bleu_score import corpus_bleu
score1 = corpus_bleu(ref_list, sum_list, weights=(1,0, 0, 0))
score2 = corpus_bleu(ref_list, sum_list, weights=(0,1, 0, 0))
print("BLEU-1: " + str(score1))
print("BLEU-2: " + str(score2))