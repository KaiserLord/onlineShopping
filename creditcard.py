from payment import Payment

class CreditCard(Payment):
    """! child class of Payment
    users can make payment via credit card
    """

    def __init__(self, paymentAmt, cardNumber:str, cardType:str):
        Payment.__init__(self, paymentAmt)
        """"! class initialiser
        @param paymentAmt payment amount
        @param cardNumber card number
        @param cardType card type
        """
        self.paymentAmt = paymentAmt
        self.cardNumber = cardNumber
        self.cardType = cardType

    def getCardDetails(self):
        """! method card details"""
        return self.cardType
    
if __name__ == '__main__':
    c = CreditCard(100.05, 'cardNumber', 'cardType')
    ty = c.getCardDetails()
    print(ty)
    # ok