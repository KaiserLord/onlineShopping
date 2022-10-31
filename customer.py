from person import Person
from controller import Controller
from shoppingcart import ShoppingCart
from product import Product


class Customer(Person):
    """! The Customer class
    child class of class Person
    inherits class Person's attributes and methods
    customers can add/remove products in their shopping carts,
    view and checkout from their shopping carts
    """

    def __init__(self, personName:str, shoppingCart):
        Person.__init__(self, personName)
        """! The class initialiser
        @param personName customers'names
        @param ShoppingCart customers' shopping cart
        """
        self.personName = personName
        self.ShoppingCart = shoppingCart #obj

        print('This Customer class')
    
    def getName(self):
        """! Get Customers' names"""
        return self.personName

# 调用controller
    def addProduct(self, product:Product) -> bool:
        """! Customers can add products in their shopping carts"""
        print(product)
        sreLen = len(self.ShoppingCart.productList)
        cart = Controller.addToCart(product, self.ShoppingCart)# 把product加入到用户personName中
        
        if sreLen < cart:
            print('customer addProduct success')
            return True

        return False


    def removeProduct(self, product:Product) -> bool:
        """! Customers can remove products from their shopping carts"""

        sreLen = len(self.ShoppingCart.productList)
        cart = Controller.removeFromCart(product, self.ShoppingCart)# 把product加入到用户personName中
        # 通过list的长度判断移除操作是否成功
        if sreLen > cart:
            return True
        
        return False

    def viewCart(self):
        """! Customers can view their shopping carts"""
        Controller.viewCart(self.ShoppingCart) #显示购物车item


    def checkOut(self):
        """! Customers can check out for the products in their shopping carts"""
        Controller.checkOut(self.ShoppingCart) #对购物车进行结账



if __name__ == '__main__':
    p1 = Product(101, 'Retro Skateboard', 20.00, 1)
    p2 = Product(102, 'Swim Seat', 15.00, 1)
    productList = []
    productList.append(p1) #传入到购物车的是list
    productList.append(p2)

    sh = ShoppingCart(productList)
    c = Customer('理查德', sh)

    c.addProduct(p1)
    c.removeProduct(p1)
    c.viewCart()
    c.checkOut()
