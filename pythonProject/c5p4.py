print("Sreekanth pradeep")
print("roll no:52")
from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
 print(grams)