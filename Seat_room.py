r, c = int(input()), int(input())
room = int(input())
cse, eee, mech = 0, 0, 0
for rm in range(room):
    for i in range(r):
        a = []
        b=[]
        for j in range(c):
            if(i % 2 == 0):
                if(i % 2 == 0) and (j%2==0):
                    a.append('cse'+str(cse))
                    cse+=1
                else:
                    a.append('eee'+str(eee))
                    eee+=1
            else:
                if(i % 2 == 1) and (j % 2 == 0):
                    a.append('mech'+str(mech))
                    mech+=1
                else:
                    a.append('cse'+str(cse))
                    cse+=1
        b.append(a)
        print(*b)
    print()
