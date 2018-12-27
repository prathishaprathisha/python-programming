def countOccurrences (s, K): 
  n = len(s) 
 b1 = 0
 b2 = 0
b= 0
 for i in range(n): 
 if s[i] == 'a': 
 if s[i] == 'b':
 b1+= 1     
 b2+= 1 
 b += b1  
return b * K + (K * (K - 1) / 2) * b1 * b2 
S = "abcb"
k = 2
print (countOccurrences(S, k)) 
