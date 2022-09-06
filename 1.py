a = float(input("Введите число"))
a = list(str(a))
myMax = 0
for i in range(len(a)):
    if a[i] == ".":
        i=i+1
    else:    
        myMax = myMax + int(a[i])
        print(i+1,"Число")       
print(myMax,"Результат")
    