import nltk

data_dir = "../project-data/"
text_paths = [
        "Adventures of Huckleberry Finn/Mark Twain_The Adventures of Huckleberry Finn.txt"
        ,"Atlas Shrugged/rand_atlas.txt"
        ,"Dracula/stoker_dracula.txt"
        ,"Emma/austen_emma.txt"
        ,"Fahrenheit 451/bradbury_fahrenheit.txt"
        ,"Jane Eyre/bronte_jane.txt"
        ,"Julius Caesar/shakespeare_caesar.txt"
        ,"the Alchemist/coelho_alchemist.txt"
        ,"the Bell Jar/plath_belljar.txt"
        ,"the Grapes of Wrath/steinbeck_grapes.txt"
        ,"the Hobbit/tolkien_hobbit.txt"
        ]


def get_word_count(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return len(tokens)


wc_dict = dict()
for path in text_paths:
    wc_dict[path.split("/")[0]] = get_word_count(data_dir+path)

import csv
with open("word_counts.csv", "w") as f:
    w = csv.DictWriter(f, wc_dict.keys())
    w.writeheader()
    w.writerow(wc_dict)

