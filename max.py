import random

liste=[]
for i in range(20):
  liste.append(random.randint(0,100))
print(liste)

maxi = liste[0]

for element in liste:
  #print(element)
  if element>maxi:
    maxi=element
print(maxi)

import random

liste2=[]
for i in range(20):
  liste2.append(random.randint(0,100))
print(liste2)

mini = liste2[0]

for element in liste2:
  #print(element)
  if element<mini:
    mini=element
print(mini)
