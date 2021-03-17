with open("E:/Sem V/Python/temp.txt", 'r') as f:
    data = f.readlines()
    print(data)
    for i in data:
        a = i.rstrip('\n').split(' ')
        avg = (float(a[1])+float(a[2])+float(a[3])+float(a[4]))/(len(a)-1)
        print(avg)
        l=[avg]
    print(max(l))


