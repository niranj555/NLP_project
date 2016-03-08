import re
import nltk

text =open('antax.txt').read()

EndPunctuation = re.compile(r'([\.\?\!]\s+)')
NonEndings = re.compile(r'(?:Mrs?|Jr|\W+|\W+(\n)\W+|i\.e)\.\s*$')
parts = EndPunctuation.split(text)
sentence = []
for part in parts:
  if len(part) and len(sentence) and EndPunctuation.match(sentence[-1]) and not NonEndings.search(''.join(sentence)):
    print(''.join(sentence))
    sentence = []
  if len(part):
    sentence.append(part)
if len(sentence):
  print(''.join(sentence))
