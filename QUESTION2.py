item = [ {'name': 'Bike', 'price':100}, 
{'name': 'TV', 'price':200},
{'name': 'Album', 'price':10}, 
{'name': 'Book', 'price':5}, 
{'name': 'Phone', 'price':500}, 
{'name': 'Computer', 'price':1000} 
]

#QUESTION1

maximum=item[0]['price']
for x in range(0,len(item)):
  y=item[x]['price']
  if y <=maximum:
    maximum=item[x]['price']
    pro=item[x]
print(pro)

#QUESTION 2


maximum=item[0]['price']
for x in range(0,len(item)):
  y=item[x]['price']
  if y >=maximum:
    maximum=item[x]['price']
    pro=item[x]
print(pro)

#  question 3
  
sum=0 
for x in range(0,len(item)):
  sum=sum+item[x]['price']
print(sum)


#QUESTION4
sum=0 
for x in range(0,len(item)):
    if item[x]['price']<10:
        item[x]['price']=0
    sum=sum+item[x]['price']
  
print(sum)