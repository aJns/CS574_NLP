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



def retrieve_tokens(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    tokens = nltk.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = list(filter(lambda word: word.lower() not in stopwords and word.isalpha(), tokens))
    return tokens



for path in text_paths:
    tokens = retrieve_tokens(data_dir+path)
    fd = nltk.FreqDist(tokens)
    fd.plot(30, cumulative=False)

