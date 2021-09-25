list1 = [1,2,3,4,5,6]
list2 = ['one','two','four','five']

# ziped

# zipped = list(zip(list1,list2))
# print(zipped)

# Unziped

# unzipped = list( zip(*zipped) )
# print(unzipped)

# for (l1,l2) in zip(list1,list2):
#     print(l1)
#     print(l2)

items = ['Apple','Banana','Orange']
counts = [3,4,6]
price = [30,25,50,100,]

sentances = []
for (item,count,price) in zip(items,counts,price):
    item,count,price = str(item),str(count),str(price)
    sentance = 'I bought ' + count + ' ' + item + 's at ' + price + '.'
    sentances.append(sentance)
    
print(sentances)