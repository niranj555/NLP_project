import nltk

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



input=open('antax.txt').read()

output=sentencerFormer(input)

print output
