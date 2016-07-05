# Multi-file Summarizer of newspaper articles:

The python file- multifile_summarizer.py takes the input from the articles 'news.txt' and 'news2.txt'. Then an algorithm is applied from the tf-idf scores of each word in the file is calcuated. After that, the sentence is given the tf-idf weight based on its words. The top weighted sentences are written in the file 'summary.txt'. Presently, the text file contains the condensed information regarding the 'news.txt' and 'news2.txt'.

   The chunkersumm.py takes input from the 'summary.txt'. Using the chunkparser, all the proper nouns are extracted and their respective sentences are stored in a dictionary of lists.
   
     'thelist' data structure stores this dictionary of lists with words as the key value and their sentences in the respective lists. 
