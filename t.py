# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
import codecs
import glob
import os
import re
import math

corpus = ""

for file in glob.glob(os.path.join('eco', u'*')):

    if os.path.isfile(file):
      # print( file )
      f=codecs.open(file,encoding='utf-8')
      for line in f:
         # print( line )
         if len(line)> 3:
            corpus+=(line)
      f.close()


corpus = re.sub("[a-zA-z]|\[\d+\]","",corpus)
corpus = re.sub("\+|»|\s.\s|-|–|_|•|“|”|'|\"|\(|\)|،|,|:|/|ó|í|ç|؟|!|\|"," ",corpus)
corpus = re.sub("\d.\d.\d"," ",corpus)
corpus = re.sub("\d.\d"," ",corpus)

corpus = re.sub("\."," @ @ ",corpus)
corpus = re.sub("\n","\n @ @ ",corpus)

output=codecs.open("monica.txt","w",encoding="UTF-8")

output.write(corpus)