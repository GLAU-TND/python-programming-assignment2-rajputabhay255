l=list(map(str,input().split()))
# string list
# l.sort(reverse=true)
l.sort(key=len)
print(l)
l.sort(reverse=True, key=lambda x:x[0])
print(l)
out=''.join(l)
#joining
print(out)
