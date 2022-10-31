from payment import Payment

class Bank(Payment):
    """! Bank class
    child class of Payment
    """

    def __init__(self, paymentAmt, bankAccount:str, bankName:str):
        Payment.__init__(self, paymentAmt)
        """! class initialiser
        @param paymentAmt payment amount
        @param bankAccount bank account 
        @param bankName bank name
        """
        self.paymentAmt = paymentAmt
        self.bankAccount = bankAccount
        self.bankName = bankName
    
    def getBankDetails():
        """! method getBankDetails to get bank details"""
        pass
    
if __name__ == '__main__':
    b = Bank(100.05, 'account', 'bankName')
    print(b.paymentAmt)
    # ok
