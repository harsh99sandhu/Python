total=0
with open("E:/Sem V/Python/city.txt", 'r') as f:
    data = f.readlines()
    print(data, len(data))
    for i in data:
        l = i.rstrip('\n').split(' ')
        if(float(l[1])>10):
            print(l[0],"and its population is",l[1])

    for i in data:
        a = i.rstrip('\n').split(' ')
        total += float(a[2])
    print(total)