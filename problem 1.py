a=list(map(str,input().split()))
#making list
b=[a[0]]
for i in range(len(a)):
    for j in range(1,len(a)):
        if b[i][-1]==a[j][0]:
            b.append(a[j])
            a.remove(a[j])
            break
print(b)