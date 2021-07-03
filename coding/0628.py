def counting(n):
 count = 1
 result = ''
 n = n + '\0'
 for i in range(1,len(n)):
     if n[i-1] == n[i]: count += 1
     else:
         result += n[i-1] + str(count) + counting(n[i:])
         break
 return result

print(counting('aaabbcccccca'))

n = 'abc' + '\0'
print(n[3])
