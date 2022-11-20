x = [10,23,24,35,65,78,90]
even = []
odd = []
for i in range(len(x)):
   if x[i]%2 == 0:
     even.append(x[i])
else:
     odd.append(x[i])
print("Even numbers are:",even)
print("Odd numbers are:",odd)
        
q = {'val1':10,'val2':20,'val3':23,'val4':22,'val5':27}
for i in q.values():
    if i % 2 ==1:
     print(i,end=" ")
    else:
       pass

w = [23, 'Python', 23.98]
z = []
for i in range(len(w)):
   z.append(type(w[i]))
   print(w)
print(z)

m = [23,4,-6,23,-9,21,3,-45,-8]
pos = []
neg = []
for i in range(len(m)):
    if m[i] > 0:
      pos.append(m[i])
      print("Positive numbers are:",pos)
    else:
      neg.append(m[i])
      print("Negative numbers are:",neg)