class Payment():
    """! Class Payment
    parent class
    """

    def __init__(self, paymentAmt:float):
        """! the initialiser
        @param paymentAmt payment amount
        """
        self.paymentAmt = paymentAmt
    
    def __str__(self):
        return '\npamentAmt:{}'.format(self.paymentAmt)


