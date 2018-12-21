mterms = 10
mterms = int(input("How many terms? "))
first two terms
m1 = 0
m2 = 1
count = 0
if mterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       mth = m1 + m2
       m1 = m2
       m2 = mth
       count += 1
