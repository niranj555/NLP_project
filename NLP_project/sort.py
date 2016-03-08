#-*- coding: utf-8 -*-

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams, trigrams
import math


stopwords = nltk.corpus.stopwords.words('english')
tokenizer = RegexpTokenizer("[\w]+")#, flags=re.UNICODE


def freq(word, doc):
    return doc.count(word)


def word_count(doc):
    return len(doc)


def tf(word, doc):
    return 1+log((freq(word, doc) / float(word_count(doc))))


def num_docs_containing(word, list_of_docs):
    count = 0
    for document in list_of_docs:
        if freq(word, document) > 0:
            count += 1
    return 1 + count


def idf(word, list_of_docs):
    return log(len(list_of_docs)/float(num_docs_containing(word, list_of_docs)))


def tf_idf(word, doc, list_of_docs):
    return (tf(word, doc) * idf(word, list_of_docs))

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

def sorte(output,count):
    order=[w for w in count]
    count.sort(reverse=True)
    lout=[]
    for i in range(max(len(count)/8,5)):
        lout.append((order.index(count[i]),count[i]))
           
     

    lout.sort(key=lambda l:l[0])
    return lout
   
   



#Compute the frequency for each term.
vocabulary = []
docs = {}
all_tips = []
antrax=open('news.txt').read()

for tip in ([antrax]):
    tip=tip.encode('punycode') 
    tokens = tokenizer.tokenize(tip)#.text
   

   # bi_tokens = bigrams(tokens)
   # tri_tokens = trigrams(tokens)
   # tokens = [token.lower() for token in tokens if len(token) > 2]
   # tokens = [token for token in tokens if token not in stopwords]

   # bi_tokens = [' '.join(token).lower() for token in bi_tokens]
    #bi_tokens = [token for token in bi_tokens if token not in stopwords]

    #tri_tokens = [' '.join(token).lower() for token in tri_tokens]
    #tri_tokens = [token for token in tri_tokens if token not in stopwords]

    final_tokens = []
    final_tokens.extend(tokens)
    #final_tokens.extend(bi_tokens)
    #final_tokens.extend(tri_tokens)
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
dicta={}
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
   


dicta[',']=0
dicta['(']=0
dicta[')']=0
dicta[';']=0
dicta['60,000']=0

#output=sentencerFormer(antrax)




for doc in docs:
    #doc.encode('ascii','ignore')
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
         #print count[i]


#for i in range(len(count)):
 #   print count[i]

total=sum(count)

summ=sorte(output,count)

f=open('summary.txt','w')

for i in range(len(summ)):
    f.write(' '.join(output[summ[i][0]])+".\n")

f.close()
      

#for item in sorted(words.items(), key=lambda x: x[1], reverse=True):
 #   print "%f <= %s" % (item[1], item[0])


