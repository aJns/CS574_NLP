import nltk
from collections import defaultdict

data_dir = "../project-data/"
text_paths = [
        # "Adventures of Huckleberry Finn/Mark Twain_The Adventures of Huckleberry Finn.txt"
        # ,"Atlas Shrugged/rand_atlas.txt"
        # ,"Dracula/stoker_dracula.txt"
        # ,"Emma/austen_emma.txt"
        "Fahrenheit_451/bradbury_fahrenheit.txt"
        # ,"Jane Eyre/bronte_jane.txt"
        # ,"Julius Caesar/shakespeare_caesar.txt"
        ,"the_Alchemist/coelho_alchemist.txt"
        # ,"the Bell Jar/plath_belljar.txt"
        # ,"the Grapes of Wrath/steinbeck_grapes.txt"
        ,"the_Hobbit/tolkien_hobbit.txt"
        ]


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def retrieve_tokens(text):
    tokens = nltk.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = list(filter(lambda word: word.lower() not in stopwords and word.isalpha(), tokens))
    tagged = nltk.pos_tag(tokens)
    noun_tagged = list(filter(lambda tandw: tandw[1] == 'NN' or tandw[1] == 'NNP', tagged))
    noun_tokens = list(map(lambda tandw: tandw[0], noun_tagged))

    return noun_tokens


def get_noun_freqs(text):
    nouns = map(lambda t: t.lower(), retrieve_tokens(text))

    freq = defaultdict(int)
    for n in nouns:
        freq[n] += 1
    # frequencies normalization and filtering
    m = float(max(freq.values()))
    for w in list(freq):
      freq[w] = freq[w]/m
    return freq


if __name__ == "__main__":
    for path in text_paths:
        text = read_file(data_dir+path)
        tokens = retrieve_tokens(text)
        freqs = get_noun_freqs(text)
        print(freqs)
        fd = nltk.FreqDist(tokens)
        fd.plot(30, cumulative=False)
