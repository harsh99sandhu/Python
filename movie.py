dubli=[]
s=set()
with open("E:/Sem V/Python/movie.txt", 'r+') as f:
    data = f.readlines()
    print(data, len(data))
    #w=["\nWar Amit 180 2019\n"]
    #f.writelines(w)
    #f.seek(0)
    #data = f.readlines()
    #print(data, len(data))

    for i in data:
        l = i.rstrip('\n').split(' ')
        if (int(l[2]) > 80):
            print(l[0], "and its production is", l[2])

    f.seek(0)
    data_1 = f.readlines()[:2]
    print(data_1)
    print(data)

    for i in data:
        l = i.rstrip('\n').split(' ')
        dubli.append(l[1])

    for i in dubli:
        if(dubli.count(i)>1):
            s.add(i)
    print(s)


