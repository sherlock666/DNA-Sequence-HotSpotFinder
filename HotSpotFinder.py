# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:21:32 2019

@author: v-chechu
"""

import re 
import pandas as pd

genes1= pd.Series()
groups1= pd.Series()
locs=pd.Series()

genes2= pd.Series()
groups2= pd.Series()
datas= pd.Series()

##### Generate Dataframe1 for hotspot_file
hotspot_file = open('HotSpot.txt','r') #load hotspot_file 
#print(hotspot_file.read()) #for print test
hotspot_file_data=hotspot_file.read().replace("\n"," ").replace("	"," ").replace("	"," ")
#print(hotspot_file_data) #for print test
tmp_hot= re.split(r" ",hotspot_file_data)
#print(tmp_hot) #for print test
for i in range (0,375):
    #print (i) #for check
    a = i % 3
    #print(a)  #for check  
    if a == 0 :
        #print ("a" ,i) #for check
        genes1=genes1.append(pd.Series(tmp_hot[i])).reset_index(drop=True)
    elif a == 1 :
        #print("b",i)
        groups1=groups1.append(pd.Series(tmp_hot[i])).reset_index(drop=True)
    elif a == 2 :
        #print ("c" ,i) #for check
        locs=locs.append(pd.Series(tmp_hot[i])).reset_index(drop=True)

df1 = pd.DataFrame({'Genes':genes1,"Groups":groups1,"Locs":locs})
df1[['Genes',"Groups","Locs"]]

##### Generate Dataframe1 for PDB_fasta_file
PDB_fasta_file = open('PDB_fasta.txt','r') #load PDB_fasta_file
#print(PDB_fasta_file.read()) #for print test
PDB_fasta_file_data=PDB_fasta_file.read().replace(">1A4Y:A","1A4Y:A").replace(">",":").replace("\n","").replace("|PDBID|CHAIN|SEQUENCE",":").replace("::",":")
#print(PDB_fasta_file_data) #for print test
tmp_PDB = re.split(r":",PDB_fasta_file_data)
#print(tmp1_PDB) #for print test
for i in range (0,186):
    #print (i) #for check
    a = i % 3
    #print(a)  #for check  
    if a == 0 :
        #print ("a" ,i) #for check
        genes2=genes2.append(pd.Series(tmp_PDB[i])).reset_index(drop=True)
    elif a == 1 :
        #print ("b" ,i) #for check
        groups2=groups2.append(pd.Series(tmp_PDB[i])).reset_index(drop=True)
    elif a == 2 :
        #print ("c" ,i) #for check
        datas=datas.append(pd.Series(tmp_PDB[i])).reset_index(drop=True)

df2 = pd.DataFrame({"Genes":genes2,"Groups":groups2,"Datas":datas})
df2[["Genes","Groups","Datas"]]

##### Left join two df

df_all = pd.merge(df1,df2,how='left', on=["Genes","Groups"])

##### Function for find loc and output former and latter 10 gene

gene_input = input ('plz gene_input: ')
group_input = input ('plz group_input: ')

ans_locs=df_all.loc[(df_all['Genes'] == gene_input) & (df_all['Groups'] == group_input)]
#print(ans_locs.Locs)
print("\nThese are Hotspot for Gene: --> "+gene_input+" <-- that you may choose :\n")
for i in ans_locs.Locs:
    print(i) #for check

hotspot_input = input ('plz hotspot_input: ')
ans_datas=df_all.loc[(df_all['Genes'] == gene_input) & (df_all['Groups'] == group_input) & (df_all['Locs'] == hotspot_input)]
for i in ans_datas.Datas:
    first = int(hotspot_input)-11
    last = int(hotspot_input)+10
    if first <= 0:
        first = 0
    if last >= len(i):
        last = len(i)
    print("\nFirst Letter Index : "+str(first))
    print("Last Letter Index : "+str(last))
    #print(i) #for check
    word = str (i)
    print("The Data Actual Length: "+str(len(word[first:last:]))+"\n")
    print(word[first:last:])
    
    








