##У нас есть массив A (заданный) и B — массив частичных сумм.
##len — длина блока

import numpy as np

a =np.numpy([12,8,19,2,3,34,85,42,12,84,6,77,5,54,9,28])
n=length = len(a)
lon= np.sqrt(n) + 1
b = [0 for _ in range(lon)]
##b=np.array(np.sum())
i=int(input())
r=int(input())
sum = 0
def de_sqrt(a, i, r) :
 for  _ in range(n) :
     b [i / lon] +=  a[i]
##Вычисляем сумму блоков
##l и r — границы
while i <= r  :
  if (i % lon == 0) and (i + lon -1 <= r) :
    sum += b[i / lon]
    i += lon
  else :
    sum += a[i]
    i += 1

print(de_sqrt(a, i, r))
print(sum)