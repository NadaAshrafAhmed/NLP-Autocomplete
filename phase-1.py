# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
import codecs
import glob
import os
import re
import math

corpus = ""

for file in glob.glob(os.path.join('corpus', u'*')):

    if os.path.isfile(file):
      # print( file )
      f=codecs.open(file,encoding='utf-8')
      for line in f:
         # print( line )
         if len(line)> 3:
            corpus+=line
      f.close()


words=re.split('\s|,|،', corpus)
w=[]
for i in words:
   if len(i)!=0:
      w+=[i]

map1={}
map11={}

count1=[0]

id=1
for i in w:
   if i in map1:
      count1[map1[i]]+=1
   else:
      map1[i]=id
      map11[id]=i
      id += 1
      count1+=[1]

# for i in range (1,100):
#    print(  count1[i]," , ",map11[i])


map2={}
map22={}

count2=[0]

id=1
for i in range (0,len(w)-1):
   ss=(w[i],w[i+1])
   if ss in map2:
      count2[map2[ss]]+=1
   else:
      map2[ss]=id
      map22[id]=ss
      id += 1
      count2+=[1]
#
# for i in range (1,100):
#    print(  count2[i]," , ",map22[i])

map3={}
map33={}

count3=[0]

id=1
for i in range (0,len(w)-2):
   ss=(w[i],w[i+1],w[i+2])
   if ss in map3:
      count3[map3[ss]]+=1
   else:
      map3[ss]=id
      map33[id]=ss
      id += 1
      count3+=[1]

# for i in range (1,100):
#    print(  count3[i]," , ",map33[i])

adj=[[]]

for i in range(0,len(map2)):
   adj+=[[]]


for i in range(1,len(map3)):
   if(map33[i][2]!='@'):
      count_of_word=count1[map1[map33[i][2]]]
      prob_with_prev_word=count2[map2[(map33[i][1],map33[i][2])]]/count1[map1[map33[i][1]]]
      prob_with_prev_prev_word=count3[map3[(map33[i][0],map33[i][1],map33[i][2])]]/count2[map2[(map33[i][0],map33[i][1])]]
      probability = math.log10(count_of_word)+math.log10(prob_with_prev_word)+math.log10(prob_with_prev_prev_word)
      adj[map2[(map33[i][0], map33[i][1])]] += [(probability,map33[i][2])]



j=0
# for i in range (1,len(adj)):
   # print(map33[i])
   # print(adj[map2[(map33[i][0], map33[i][1])]])

output=codecs.open("res.txt","w",encoding="UTF-8")

nn=0
for i in map2:
   if(len(adj[map2[i]])>0):
      nn+=1
output.write(str(nn))
output.write( "\n" )

for i in map2:
   if(len(adj[map2[i]])>0):
      adj[map2[i]].sort( key=lambda x: x[0], reverse=True )
      output.write(i[0])
      output.write("\n")
      output.write(i[1])
      output.write("\n")
      output.write(str(min(10,len(adj[map2[i]]))))
      output.write("\n")
      for j in range(min(10,len(adj[map2[i]]))):
         # output.write(str(adj[map2[i]][j][0]))
         # output.write("\n")
         output.write(adj[map2[i]][j][1])
         output.write("\n")
      # print(i)
      # print(adj[map2[i]])


