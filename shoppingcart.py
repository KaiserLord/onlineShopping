from product import Product


class ShoppingCart():
    
    def __init__(self, productList):
        """! The initialiser
        @param productList list of products in shopping cart
        """
        self.productList = productList
    
    def emptyCart(self):
        """! Empty shopping cart"""
        # 清空购物车
        self.productList = []

    def addItem(self, product):
        """! users add items into shopping cart
        @param product products being added into the shopping cart
        """
        self.productList.append(product)

        return True

    def removeItem(self, product):
        """! users remove items from shoppingcart
        @param product products that are being removed from the shoppingcart
        """
        self.productList.remove(product)

        return True
    
    def currentTotal(self):
        """! cauculates total amount for products in the shopping cart"""
        # 结账
        money = 0.0
        for item in self.productList:
            money += item.price
        print('total price:' + str(money))
        return money

    def listItem(self):
        """! list of items in shipping cart"""
        # 显示购物车所有内容
        for item in self.productList:
            print(item)


if __name__ == '__main__':
    p1 = Product(101, 'Retro Skateboard', 20.00, 1)
    p2 = Product(102, 'Swim Seat', 15.00, 1)
    productList = []
    productList.append(p1) #传入到购物车的是list
    productList.append(p2)
    
    s = ShoppingCart(productList)
    # ok
