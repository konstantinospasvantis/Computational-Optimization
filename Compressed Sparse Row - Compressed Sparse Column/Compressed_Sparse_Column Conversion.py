# -*- coding: utf-8 -*-
"""Σαμαρας_Εβδ2_Β.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10K39Pu2OOOzeVhKZfqZlpUIVc08iufQm
"""

import numpy as np

A= [[1,0,0,9,0,0],[5,0,0,0,0,0],[0,-3,0,0,2,0],[0,0,0,0,0,0],[0,0,0,2,0,0],[0,7,0,0,0,1]]
A=np.asarray(A)

Anz=[]
JA=[]
IA=np.zeros(A.shape[1]+1)
dcol=True
nz=0
k=0
for j in range(A.shape[1]):
  for i in range(A.shape[0]):
    if np.all(A[:,j]==0) :
      k=k+1
      if j==A.shape[1]-1:
        IA[-1]=nz+1
        if dcol:
          if IA[j-1]==0:
            for v in range(k):
              IA[j-v]=nz+1
              dcol=False
          elif IA[j]==0:
            IA[j]=nz+1
      break
    elif A[i][j]==0:
      pass
    elif A[i][j]!=0:
      Anz.append(A[i][j])
      JA.append(i+1)
      nz=nz+1
      if dcol:
        if j==0:
          IA[j]=nz
          dcol=False

        elif IA[j-1]==0:
          for v in range(k+1):
            IA[j-v]=nz
            dcol=False
            k=0
        
        else:
          IA[j]=nz
          dcol=False
  IA[-1]=nz+1
  dcol=True


print(Anz)
print(JA)
print(IA)
