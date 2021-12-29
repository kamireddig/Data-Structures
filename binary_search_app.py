n = int(input('Enter values : '))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
lst = sorted(lst)
print(lst)

t = int(input('Enter the Target Search element : '))
l = lst[0]
r = lst[n-1]
m = int((l + r)/2)

counter = 0
while(m != t):
    counter = counter + 1
    if m < t:
        l = m
        m = int((l + r)/2)
    elif m > t:
        r = m
        m = int((l+r)/2)
    else:
        m

l,m,r,t = int(l), int(m), int(r), int(t)

# print('Target Search Element is :',t)
print('Initial First Element : ',l)
print('Initial Last Element : ',r)

print('Finally, Found the Element ', m, ' in ', counter, ' steps')