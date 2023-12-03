import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.set_printoptions(threshold=np.inf)
arxeio = input('type the file name with .mps extension you want to convert and press Enter:  \n')
print('This may take a bit')
f=open(arxeio ,'r')

s=f.readline()
s=f.readline()
s=f.readline()
#ROWS ta vazoyme se dict
eq_type=dict()
m=0
while s[:7] != 'COLUMNS':
  if s[1:3].strip() in ['E','L','G']:
    rowlabel=s[4:12].strip()
    eq_type[rowlabel]=s[1:3].strip()
    m=m+1
  elif s[1:3].strip() == 'N' :
    name_obj=s[4:12].strip()
  s=f.readline()


#EXOUME VALEI TIS GRAMMES ME TA E L G SE ENA DICT
s=f.readline()
arith={list(eq_type.keys())[i]:list(range(0,m+1))[i] for i in range(m)}
A=np.zeros(m)
a=np.zeros(m)
n=0
dict_obj=dict()
metav={s[4:12].strip():0}


while s[:3]!= 'RHS' :
    if s[4:13].strip() in metav :
        if s[14:22].strip() in arith :
            a[arith[s[14:22].strip()]]=float(s[24:36].strip())
            if s[39:47].strip() in arith :
                a[arith[s[39:47].strip()]]=float(s[49:61].strip())
            elif s[39:47].strip() == name_obj :
                dict_obj[s[4:12].strip()]=float(s[49:61].strip())
            elif s[39:47].strip()=='':
                pass
        elif s[14:22].strip() == name_obj :
            dict_obj[s[4:12].strip()]=float(s[24:36].strip())
            if s[39:47].strip() in arith :
                a[arith[s[39:47].strip()]]=float(s[49:61].strip())
            elif s[39:47].strip() == '' :
                pass


    elif s[4:13].strip() not in metav :
        n=n+1
        A=np.vstack([A,a])
        a=np.zeros(m)
        metav[s[4:12].strip()]=n
        if s[14:22].strip() in arith :
            a[arith[s[14:22].strip()]]=float(s[24:36].strip())
            if s[39:47].strip() in arith :
                a[arith[s[39:47].strip()]]=float(s[49:61].strip())
            elif s[39:47].strip() == name_obj :
                dict_obj[s[4:12].strip()]=float(s[49:61].strip())
            elif s[39:47].strip()=='':
                pass
        elif s[14:22].strip() == name_obj :
            dict_obj[s[4:12].strip()]=float(s[24:38].strip())
            if s[39:49].strip() in arith :
                a[arith[s[39:49].strip()]]=float(s[49:61].strip())
            elif s[39:49].strip() == '' :
                pass

    s=f.readline()

n=n+1
A=np.vstack([A,a])
A=np.delete(A,0,axis=0)
A=np.transpose(A)

#Exw teleiwsei me ton A , exw vrei diastaseis

s=f.readline()
b=np.zeros(m)
while s[:6] != 'ENDATA' :
    if s[14:23].strip() in arith :
        b[arith[s[14:22].strip()]]=float(s[24:36].strip())
        if s[39:47].strip() in arith :
            b[arith[s[39:47].strip()]]=float(s[49:61])
        elif s[39:47].strip() == '' :
            pass
    s=f.readline()

b=np.asarray(b)
c=np.zeros(n)
for i in dict_obj :
    c[metav[i]]=dict_obj[i]

Eqin=np.zeros(m)
for i in arith :
    if eq_type[i] == 'E' :
        Eqin[arith[i]]= 0
    elif eq_type[i] == 'G' :
        Eqin[arith[i]] = 1
    elif eq_type[i] == 'L' :
        Eqin[arith[i]] = -1
Eqin = np.asarray(Eqin)


c=np.asarray(c)
c=np.transpose(c)
f.close()



i=1
file_1=open('Final','w+')
#write A
file_1.write('A = [' + str(A[0]) + '\n')
while i < m:
    file_1.write(' ' * 5 + str(A[i]) + '\n')
    i = i + 1

file_1.write('\n' * 2)

#write b
i=1
file_1.write('b = [' + str(b[0]) + '\n')
while i < len(b)-1 :
    file_1.write(' ' * 5 + str(b[i]) + '\n')
    i=i+1
file_1.write(' '*5 + str(b[i]) + ']')
file_1.write('\n'*2)
#write c
i=1
file_1.write('c = [' + str(c[0]) + '\n')
while i < len(c)-1 :
    file_1.write(' ' * 5 + str(c[i]) + '\n')
    i = i + 1
file_1.write(' ' * 5 + str(c[i]) + ']')
file_1.write('\n'*2)
#write Eqin
i=1
file_1.write('Eqin = [' + str(Eqin[0]) + '\n')
while i < len(Eqin)-1 :
    file_1.write(' ' * 5 + str(Eqin[i]) + '\n')
    i = i + 1
file_1.write(' ' * 5 + str(Eqin[i]) + ']')
file_1.write('\n'*2)
file_1.write('MinMax = -1')
file_1.close()




print('Done, your txt file is named final')
