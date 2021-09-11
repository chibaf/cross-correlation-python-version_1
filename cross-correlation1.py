# very slow version
import csv
import sys
import collections
import matplotlib.pyplot as plt

def inner_product(vec1,vec2):
  sum=0.0
  for i in range(len(vec1)):
    sum=sum+vec1[i]*vec2[i]
  return sum

mtrx=[]
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      if len(row)==3:
        a=[float(row[0]),float(row[1]),float(row[2])]
        mtrx.append(a)
rez = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]  #transpose a matrix

# computation of cross-correlation
corr=[]
x=collections.deque(rez[2])
for i in range(len(rez[2])+1):
  x.append(x.popleft())
  corr.append(inner_product(x,rez[2]))
print(corr)
#plt.plot(corr)