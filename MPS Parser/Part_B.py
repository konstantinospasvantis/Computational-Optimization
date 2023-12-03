import numpy as np
arxeio = input('type the file name with .txt extension you want to convert and press Enter:  \n')
f=open(arxeio,'r')
s=f.readline(3)
s=f.readline()
A=np.fromstring(s,dtype=float,sep=' ')
s=f.readline()
while s[0] != 'b' :
    if s[0:3].strip() == '' :
        break
    elif s[-2] ==']' :
        a=s[:-2]
        A1=np.fromstring(a,dtype=float,sep=' ')
        A=np.vstack([A,A1])
    else:
        A1=np.fromstring(s,dtype=float,sep=' ')
        A=np.vstack([A,A1])
    s=f.readline()
s=f.readline(3)
s=f.readline()
b=list()
i=0
while s[0] != 'c' :
    if s[0:20].strip() == '':
        break
    elif s[-2] == ']' :
        b1=float(s[:-2].strip())
        b.insert(i,b1)
    else:
        b1=float(s.strip())
        b.insert(i,b1)
    s=f.readline()
    i=i+1
s=f.readline(3)
s=f.readline()
c=list()
i=0
while s[0] != 'E' :
    if s[0:20].strip() == '':
        break
    elif s[-2] == ']' :
        c1=float(s[:-2].strip())
        c.insert(i,c1)
    else:
        c1=float(s.strip())
        c.insert(i,c1)
    s=f.readline()
    i=i+1
s=f.readline(6)
s=f.readline()
Eqin=list()
i=0
while s[0] != 'M' :
    if s[0:20].strip() == '':
        break
    elif s[-2] == ']' :
        E1=float(s[:-2].strip())
        Eqin.insert(i,E1)
    else:
        E1=float(s.strip())
        Eqin.insert(i,E1)
    s=f.readline()
    i=i+1
f.close()
#############################################
arper=A.shape[0]
armet=A.shape[1]

Rows=dict()
for i in range(arper):
    Rows['PER'+str(i)]=Eqin[i]

for i in Rows :
    if Rows[i] == -1:
        Rows[i]='L'
    elif Rows[i] == 0:
        Rows[i]='E'
    elif Rows[i]==1:
        Rows[i]='G'

RHS=dict()
q=0
for i in Rows:
    RHS[i]=b[q]
    q=q+1
OBJSYNT=dict()
for i in range(armet):
    OBJSYNT['X'+str(i)]=c[i]

##exw vrei listes

file_1=open('Final','w+')
file_1.write('NAME' + ' '*10 + 'Final' + '\n')
file_1.write('ROWS' + '\n')

for i in Rows:
    file_1.write(' ' + Rows[i] + ' '*2 + i + '\n')

file_1.write(' ' + 'N' + ' '*2 +  'COST' + '\n' )
file_1.write('COLUMNS\n')
mystring='{0:>6}{1:>12}{2:>18}\n'
for n in range(armet):
    for m in range(arper):
        file_1.write(mystring.format(list(OBJSYNT.keys())[n],list(Rows.keys())[m],str(A[m][n])))
    if list(OBJSYNT.keys())[n] in OBJSYNT:
        file_1.write(mystring.format(list(OBJSYNT.keys())[n],'COST',str(list(OBJSYNT.values())[n])))

file_1.write('RHS\n')
my_string2='{0:>5}{1:>13}{2:>18}\n'
for i in RHS:
    file_1.write(my_string2.format('B',i,RHS[i]))
file_1.write('ENDATA')
file_1.close()

print('Done, your txt file is named "final"')


