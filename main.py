lst1= list(range(2,10))
lst2= list(range(1,10))
print(lst1)
for num1 in lst1:
  for num2 in lst2:
    print(" {} * {} = {} \n".format(num1,num2, num1*num2))

