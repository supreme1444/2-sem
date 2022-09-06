def funct(x):
    return pow(1+1/x,x)
n=int(input())
dict={}
for i in range(1,n+1):
    dict[i]=funct(i)
print(sum(dict))
