class Bank:
    ac_num: int
    name:str
    ac_type: str
    ifsc_code: str
    branch: str
    balance: int

    def set_bnk(self, acn,ac_type ,name, ifsc,branch, balance):
        self.ac_num = acn
        self.name = name
        self.ac_type = ac_type
        self.ifsc_code = ifsc
        self.branch = branch
        self.balance = balance
    def display_bnk(self):
        print(self.ac_num, self.name,self.ac_type ,self.ifsc_code, self.branch, self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print(f'your balance is {self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficent funds")
        else:
            self.balance-= amount
            print(f"your balance is {self.balance}'")
    def get_balance(self):
        print(f'your balance is {self.balance}')


bank1 = Bank()
bank1.set_bnk(48501484868, "john", "savings","hdfc1458171", "thripunithura", 4000000000)
bank1.display_bnk()
bank1.deposit(1000)
