import nltk

tokenizer = nltk.RegexpTokenizer(r'\w+')

f = open("./data/stopwords-fi.txt")
stopWords = tokenizer.tokenize(f.read())
f.close()

f = open("./data/article0.txt")
text = f.read()
f.close()
words = tokenizer.tokenize(text)


freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords or len(word) < 2:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


sentences = nltk.sent_tokenize(text)
sentenceValue = dict()


for sentence in sentences:
    for wordValue in freqTable.items():
        if wordValue[0] in sentence.lower():
            if sentence[:12] in sentenceValue.items():
                sentenceValue[sentence[:12]] += wordValue[1]
            else:
                sentenceValue[sentence[:12]] = wordValue[1]


sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

weight = 1

summary = ''
for sentence in sentences:
        if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (weight * average):
            summary +=  " " + sentence

print("\nPrinting summary...\n#############################################\n")
print(summary)
