import nltk
import csv
import os

data_dir = "../project-data"


def get_word_count(file_path):
    tokens = list()
    with open(file_path, 'r') as f:
        try:
            text = f.read()
            tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(text)
        except UnicodeDecodeError:
            print("Couldn't read ", file_path)

    return len(tokens)

def compile_path_list(path_list, rootdir):
    for root, _, files in os.walk(rootdir):
        for f in files:
            if f.endswith('.txt'):
                path_list.append(os.path.join(root, f))



text_paths = list()
compile_path_list(text_paths, data_dir)
wc_dict = dict()
for path in text_paths:
    wc_dict[path] = get_word_count(path)


with open("word_counts.csv", "w") as f:
    w = csv.DictWriter(f, wc_dict.keys())
    w.writeheader()
    w.writerow(wc_dict)

