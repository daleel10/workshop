class ATM():
    # initialize valid papers
    allowed_papers = [100,50,20,10,5,4,3,2,1]

    def __init__(self,balance,bank_name):
        self.balance = balance
        self.bank_name = bank_name
    def withdraw(self,request):


        initial_req = request # in order to keep track the initial request/ this is usefull when we will update the balance
        
        print("Welcome to " + self.bank_name)
        print("Current balance = " + str(self.balance))
        print("=============================")
        
        if self.balance < request: 
            print("Can't give you all this money !!")
        else:
            for paper in range(len(self.allowed_papers)):
                while request > 0:
                    # verify which paper you gave him
                    if request - self.allowed_papers[paper] >= 0:
                        request -= self.allowed_papers[paper]
                        print("Give " + str(self.allowed_papers[paper]))
                     
                    else:
                        # switch to the next paper/ exit while loop
                        break
        print("=============================")

        # update balance to the new balance 
        self.balance = self.balance - initial_req
