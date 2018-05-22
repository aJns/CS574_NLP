import nltk

# text_path = "./project-data/the Alchemist/coelho_alchemist.txt"
text_path = "./project-data/Adventures of Huckleberry Finn/Mark Twain_The Adventures of Huckleberry Finn.txt"

with open(text_path, 'r') as f:
    text = f.read()

tokens = nltk.word_tokenize(text)

stopwords = nltk.corpus.stopwords.words('english')

tokens = list(filter(lambda word: word.lower() not in stopwords and word.isalpha(), tokens))

fd = nltk.FreqDist(tokens)
fd.plot(30,cumulative=False)

