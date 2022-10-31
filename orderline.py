from product import Product


class OrderLine():
    """! Class OrderLine 
    calculate total amount for orders
    """

    def __init__(self, product: Product, qty: int):
        """! The initialiser
        @param product products include in the order
        @param qty quantatity
        """
        self.product = product
        self.qty = qty
    def __str__(self):
        return '\nproduct:{}\tqty:{}'.format(self.product.productDescription, self.qty)

    def calcTotal(self):
        """! Calculate total amount"""
        total = self.product.price * self.qty 
        #price * qty
        # orderLine是指同一类商品的购买数量，称为一项
        return total