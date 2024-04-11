def sum(curr, n):
   if curr==n:
      return n
   return curr + sum(curr +1, n)

print(sum(0, 4))
print(sum(3, 20))


