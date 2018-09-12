money = 5000
request = 113
allowed = [100,50,10,5,4,3,2,1]

if money < request:
    print('we do not have enough money.')
else:
    for paper in range(len(allowed)):
        while request > 0:
            if request - allowed[paper] >= 0:
                request -= allowed[paper]
                print('Give ' + str(allowed[paper]))
            else:
                break