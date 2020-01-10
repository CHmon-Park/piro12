def qnsgo(n):
    temp = []
    for i in range(len(n)):
        temp.append(int(n[i]))
    return temp

n = input()
if int(n)<1 or int(n)>1000000:
    print("잘못된 입력!")
else:
    a = len(n)
    todtjdwk = []

    for i in range(a*10+a, int(n)):
        mylist = qnsgo(str(i))
        sum = 0
        for j in mylist:
            sum+=j
        if i+sum == int(n):
            todtjdwk.append(i)

    if len(todtjdwk) == 0:
        print(0)
    else:
        print(min(todtjdwk))
