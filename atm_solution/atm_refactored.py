def withdrawal(balance,request):
    initial_req = request
    # initialaze allowed papers
    allowed_papers = [100,50,20,10,5,4,3,2,1]

    #check balance
    if balance < request:
        print('not enough')
    for paper in range(len(allowed_papers)):

        while request > 0 :
            if request - allowed_papers[paper] >= 0 :
                request -= allowed_papers[paper]
                print("Give " + str(allowed_papers[paper]))
            else:
                break
    return balance - initial_req