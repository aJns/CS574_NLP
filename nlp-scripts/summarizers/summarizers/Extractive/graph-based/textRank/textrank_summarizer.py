from gensim.summarization import summarizer
from nltk import sent_tokenize

"""
TextRank is based on PageRank algorithm that is used on Google 
Search Engine. Its base concept is "The linked page is good, 
much more if it from many linked page". The links between the 
pages are expressed by matrix (like Round-robin table). We can 
convert this matrix to transition probability matrix by dividing 
the sum of links in each page. And the page surfer moves the 
page according to this matrix.
"""
sample = "Rice Pudding - Poem by Alan Alexander Milne\
What is the matter with Mary Jane?\
She's crying with all her might and main,\
And she won't eat her dinner - rice pudding again -\
What is the matter with Mary Jane?\
What is the matter with Mary Jane?\
I've promised her dolls and a daisy-chain,\
And a book about animals - all in vain -\
What is the matter with Mary Jane?\
What is the matter with Mary Jane?\
She's perfectly well, and she hasn't a pain;\
But, look at her, now she's beginning again! -\
What is the matter with Mary Jane?\
What is the matter with Mary Jane?\
I've promised her sweets and a ride in the train,\
And I've begged her to stop for a bit and explain -\
What is the matter with Mary Jane?\
What is the matter with Mary Jane?\
She's perfectly well and she hasn't a pain,\
And it's lovely rice pudding for dinner again!\
What is the matter with Mary Jane?"

class TextRankSummarizer:
	"""
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut 
     or higer than max_cut will be ignored.
    """
	
	def __init__ (self):
		pass

	def summarize (self, text, ratio):
		text_list = sent_tokenize (text)
		text = "\n".join (text_list)
		return summarizer.summarize (text, ratio = ratio, split = True)

if __name__ == "__main__":
	trs = TextRankSummarizer ()
	print (trs.summarize (sample, 0.2))