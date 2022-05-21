class loan:
    def __init__(self):
        self.interestrateb=0
        self.interestratel=0

        self.__personaldetails() #added__to hide
        self.__menu()
        



    def __personaldetails(self):
        username=input("Please enter your name")
        useraadhar=int(input("Please enter your aadhar  number"))
        usernumber=int(input("Please enter your 10 digit phone number"))
    def __menu(self):

        user_input=input("""
    Hello, how would you like to proceed, press the number that suits your need:
    1. Enter 1 if you want to take loan/boorow money.
    2. Enter 2 if you want to provide loan/lend money.
    3. Enter 3 to EXIT
""")
        if user_input=="1":
            self.borrowing_money()
        elif user_input=="2":
            self.lending_money()
        elif user_input=="3":
            print("BYE")
    def totaldueborrower(self): #this variable will be used to give the amount of money the borrower will have to pay after the time duration he/she has entered
        pass

    def principle(self):  
        pass
    def totalmoneylender(self): #this variable will be used to give the amount of money the lender will get after the time duration he/she has entered
        pass
        



    def borrowing_money(self):
        user_input2=input("""
How much money do want to borrow?, enter the suitable digit:
1. Press '1' if in the range of 10,000-1,00,000 Rs (l1)
2. Press '2' if in the range of 1,00,000-10,00,000 Rs (l2)
3. Press '3' if in the range of 10,00,000-50,00,000 Rs (l3)
4. Press '4' if in the range of 50,00,000-1,00,00,000 Rs (l4)
5. Press '5' to exit
""")
        if user_input2=="1":
            self.__case1()
        elif user_input2=="2":
            self.__case2()
        elif user_input2=="3":
            self.__case3()
        elif user_input2=="4":
            self.__case4()
        elif user_input2=="5":
            print("BYE")
    def __case1(self):
        self.interestrateb=2
        intrb=self.interestrateb
        print("interest rate = 2%")
        self.principle=int(input("Please enter the exact amount of money you want to borrow"))
        prin=self.principle
        while prin<10000 or prin>100000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prin=self.principle
            
        self.timeduration=int(input("Please enter the number of months for which you want to borrow the money"))
        time=self.timeduration
        self.totaldueborrower= prin+ (((prin*intrb/100*((1+(intrb/100)**(time))))*(1+intrb/100))/(1+(intrb/100)**(time)))
        

        
        print("Please collect your money from the cash counter \nloan category l1 \nThank you for your time")
        
    def __case2(self):
        self.interestrateb=1
        intrb=self.interestrateb
        print("interest rate = 1%")
        self.principle=int(input("Please enter the exact amount of money you want to borrow"))
        prin=self.principle
        while prin<100000 or prin>1000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prin=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to borrow the money"))
        time=self.timeduration
        self.totaldueborrower= prin+ prin*(1+(intrb/(1200))**time) 
        print("Please collect your money from the cash counter \nloan category l1 \nThank you for your time")

    def __case3(self):
        self.interestrateb=0.8
        intrb=self.interestrateb
        print("interest rate = 0.8%")
        self.principle=int(input("Please enter the exact amount of money you want to borrow"))
        prin=self.principle
        while prin<1000000 or prin>5000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prin=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to borrow the money"))
        time=self.timeduration
        self.totaldueborrower= prin+ prin*(1+(intrb/(1200))**time) 
        print("Please collect your money from the cash counter \nloan category l1 \nThank you for your time")

    def __case4(self):
        self.interestrateb=0.7
        intrb=self.interestrateb
        print("interest rate = 0.7%")
        self.principle=int(input("Please enter the exact amount of money you want to borrow"))
        prin=self.principle
        while prin<5000000 or prin>10000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prin=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to borrow the money"))
        time=self.timeduration
        self.totaldueborrower= prin+ prin*(1+(intrb/(1200))**time) 
        print("Please collect your money from the cash counter \nloan category l1 \nThank you for your time")
    

    def lending_money(self):
        
        user_input3=input("""
How much money do want to lend?, enter the suitable digit:
1. Press '1' if in the range of 10,000-1,00,000 Rs
2. Press '2' if in the range of 1,00,000-10,00,000 Rs
3. Press '3' if in the range of 10,00,000-50,00,000 Rs
4. Press '4' if in the range of 50,00,000-1,00,00,000 Rs
5. Press '5' to exit
""")
        if user_input3=="1":
            self.__casel1()
        elif user_input3=="2":
            self.__casel2()
        elif user_input3=="3":
            self.__casel3()
        elif user_input3=="4":
            self.__casel4()
        elif user_input3=="5":
            print("BYE")
    def __casel1(self):
        self.interestratel=1
        intrl=self.interestratel
        print("interest rate = 1%")
        self.moneytolend=int(input("Please enter the exact amount of money you want to lend"))
        prinl=self.moneytolend
        while prinl<10000 or prinl>100000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prinl=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to lend the money"))
        timel= self.timeduration
        
        self.totalmoneylender= prinl+ prinl*(1+(intrl/(1200))**timel) 
        print("Please deposit your money at the cash counter l1, Thank you for your time")
        
    def __casel2(self):
        self.interestratel=0.5
        intrl=self.interestratel
        print("interest rate = 0.5%")
        self.moneytolend=int(input("Please enter the exact amount of money you want to lend"))
        prinl=self.moneytolend
        while prinl<100000 or prinl>1000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prinl=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to lend the money"))
        timel= self.timeduration
        
        self.totalmoneylender=prinl+ prinl*(1+(intrl/(1200))**timel)
        print("Please deposit your money at the cash counter l2, Thank you for your time")
        

    def __casel3(self):
        self.interestratel=0.4
        intrl=self.interestratel
        print("interest rate = 0.4%")
        self.moneytolend=int(input("Please enter the exact amount of money you want to lend"))
        prinl=self.moneytolend
        while prinl<100000 or prinl>5000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prinl=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to lend the money"))
        timel= self.timeduration
        
        self.totalmoneylender=prinl+ prinl*(1+(intrl/(1200))**timel)
        print("Please deposit your money at the cash counter l3, Thank you for your time")

    def __casel4(self):
        self.interestratel=0.3
        intrl=self.interestratel
        print("interest rate = 0.3%")
        self.moneytolend=int(input("Please enter the exact amount of money you want to lend"))
        prinl=self.moneytolend
        while prinl<5000000 or prinl>10000000:
            print("please enter the amount in the selected range")
            self.principle=int(input("Please enter the exact amount of money you want to borrow"))
            prinl=self.principle
        self.timeduration=int(input("Please enter the number of months for which you want to lend the money"))
        timel= self.timeduration
        
        self.totalmoneylender=prinl+ prinl*(1+(intrl/(1200))**timel)
        print("Please deposit your money at the cash counter l4, Thank you for your time")
    

  
