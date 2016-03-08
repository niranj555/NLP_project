#-*- coding: utf-8 -*-
#MULTIFILE SUMMARIZER
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams, trigrams
import math
from math import log


stopwords = nltk.corpus.stopwords.words('english')
tokenizer = RegexpTokenizer("[\w]+")#, flags=re.UNICODE


#Compute the frequency for each term.
def freq(word, doc):
    return doc.count(word)


def word_count(doc):
    return len(doc)

#Term frequency of "word" in document "doc"
def tf(word, doc):
    return 1+log((freq(word, doc)))


def num_docs_containing(word, list_of_docs):
    count = 0
    for document in list_of_docs:
        if freq(word, document) > 0:
            count += 1
    return count


#Inverse Document frequency of "word" from list of docs
def idf(word, list_of_docs):
    return log(1+(len(list_of_docs)/float(num_docs_containing(word, list_of_docs))))


def tf_idf(word, doc, list_of_docs):
    return (tf(word, doc) * idf(word, list_of_docs))


#Sentence spliter based on just full-stop.(For now)
def sentencerFormer(text):
    ftext=nltk.word_tokenize(text)
    temp=[]
    sentenceArray=[]
    for word in ftext:
        if word!='.':
           temp.append(word)
        else:
           sentenceArray.append(temp)
           temp=[]
    return sentenceArray

#Sorts the sentence weights and returns the 
def sort_weights(output,count):
    order=[w for w in count]
    count.sort(reverse=True)
    lout=[]
    for i in range(max(len(count)/3,5)):
        lout.append((order.index(count[i]),count[i]))
           
     

    lout.sort(key=lambda l:l[0])
    return lout
   
   



vocabulary = []
docs = {}
dicta={}
news=open('news.txt').read()
news2=open('news2.txt').read()

all_tips = [news,news2]


for tip in all_tips:
    tip=tip.encode('punycode') 
    tokens = tokenizer.tokenize(tip)#.text
   

 

    final_tokens = []
    final_tokens.extend(tokens)
   
    docs[tip] = {'freq': {}, 'tf': {}, 'idf': {},
                        'tf-idf': {}, 'tokens': []}

    for token in final_tokens:
        #The frequency computed for each tip
        docs[tip]['freq'][token] = freq(token, final_tokens)
        #The term-frequency (Normalized Frequency)
        docs[tip]['tf'][token] = tf(token, final_tokens)
        docs[tip]['tokens'] = final_tokens

    vocabulary.append(final_tokens)

for doc in docs:
    for token in docs[doc]['tf']:
        #The Inverse-Document-Frequency
        docs[doc]['idf'][token] = idf(token, vocabulary)
        #The tf-idf
        docs[doc]['tf-idf'][token] = tf_idf(token, docs[doc]['tokens'], vocabulary)

#Now let's find out the most relevant words by tf-idf.
words = {}

for doc in docs:
    for token in docs[doc]['tf-idf']:
        if token not in words:
            words[token] = docs[doc]['tf-idf'][token]
        else:
            if docs[doc]['tf-idf'][token] > words[token]:
                words[token] = docs[doc]['tf-idf'][token]

   # print doc
    for token in docs[doc]['tf-idf']:
      #  print token, docs[doc]['tf-idf'][token]
        dicta[token]=docs[doc]['tf-idf'][token]
   
f=open('summary.txt','w')

#To find tf-idf weights of "nouns" in each sentence of a given doc.
for doc in docs:
   
    
    output=sentencerFormer(doc)
    count=[0]*len(output)
    for i in range(len(output)):
         ps[i]=nltk.pos_tag(output[i])
         for j in range(len(output[i])):
             tag=ps[i][j][1]
             if tag.startswith('NN'):
                try:
                        count[i]=count[i]+dicta[ps[i][j][0]]
                except KeyError:
                	count[i]=count[i]+0;
    
    total=sum(count)
    print "output: \n\n"
  #  for i in range(len(output)):
  #      print output[i]

    print "\n\n"

    summ=sort_weights(output,count)

   

    for i in range(len(summ)):
        f.write(' '.join(output[summ[i][0]])+".\n")

f.close()
      





