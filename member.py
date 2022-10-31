import random
from controller import Controller
from registerUser import RegisteredUser
from order import Order
from datetime import datetime
from address import Address
from payment import Payment
from orderline import OrderLine
from product import Product
from customer import Customer
from shoppingcart import ShoppingCart
from creditcard import CreditCard
from bank import Bank

class Member(RegisteredUser,Customer):
    """! Member class, child class of RegisteredUser and Customer
    inherits parent classes' attributes and methods
    """

    def __init__(self, personName:str, username:str, password:str, 
                email:str, memberID:str, memberAddress:Address, 
                memberPhone:str, shoppingCart:ShoppingCart, orderList):
        Customer.__init__(self, personName, shoppingCart)
        RegisteredUser.__init__(self, personName, username, password, email) #指定父类的init方法
        

        """! The class initialiser
        @param personName member names
        @param username member login user names
        @param password memner login password
        @param email member emails
        @param members' shopping carts
        @param memberID member ID
        @param memberAddress member address
        @param memberPhone member phone numbers 
        @param orderList members' order lists
        """
        self.personName = personName
        self.username = username
        self.password = password
        self.email = email
        self.ShoppingCart = shoppingCart #obj
        self.memberID = memberID
        self.memberAddress = memberAddress #obj
        self.memberPhone = memberPhone
        self.orderList = orderList
        print('This is member class')
    
    def getName(self):
        """! Get members names"""
        return self.username
    
    def getAddress(self):
        """! Get members address"""
        return self.memberAddress
        


    def login(self, username, password, flag):
        """! login method allows members to login
        @param username usernames for members to login
        @param password password that members can use to login
        """
        
        # RegisteredUser.login(self, username, password, flag)
        pass
        

    
    def logout(self, username, flag):
        """! logout method allows members to log out of the system"""
        # RegisteredUser.logout(self, username, flag)
        pass

    def addProduct(self, product):
        """! members can add products to their shopping carts"""
        Customer.addProduct(self, product)
    
    def removeProduct(self, product):
        """! members can remove products from their carts"""
        Customer.removeProduct(self, product)
    
    def viewCart(self):
        """! members can view their shopping carts"""
        Customer.viewCart(self)

    def checkOut(self):
        """! members can check out for their orders"""
        Customer.checkOut(self)

    def placeOrder(self, orderData):
        """! Method that allows members to place orders"""
        # 下订单：生成订单对象
        time_now = datetime.now()
        shippingCost = random.uniform(0,1000) #运费
        orderLineCost = 0.0
        for item in orderData[2]: # 把orderLine里面的所有项目都列出来
            orderLineCost += item.calcTotal()

        ordTotal = orderLineCost + shippingCost
        ord = Order(123, 0, time_now, ordTotal, shippingCost, orderData[0], orderData[1], orderData[2])

        self.orderList.append(ord) #加入到当前会员的订单list中
        print('place order successful')
        

    def viewOrderStatus(self, ord:Order):
        """! Method that allows members to check their order status"""
        # 显示传入订单的status,把数字转换成对应的str文字
        Controller.viewOrder(ord)
        print('view order successful')
    # 直接调用Controller.viewOrder(member.ordList中的一项)
        


    def cancelOrder(self, ord:Order):
        """! Method that allows members to cancel their orders"""
        # 取消订单
        Controller.cancelOrder(self.orderList)
        print('cancel order successful')

    def viewOrders(self):
        """! Method that allows members to view their orders"""
        # 显示当前用户的所有订单
        Controller.viewAllOrder(self.orderList)
        print('view all orders successful')
        
            
    def getOrder(self, orderId):
        for item in self.orderList:
            if item.orderID == orderId:
                return item
        print('orderID:{}的订单未在数据库中收录'.format(orderId))
        

    def makePayment(self, ordDet:Order):
        """! Method that allows members to make payment for their orders"""
        Controller.makePayment(ordDet)
            
    
    def updateDeliveryAddress(self, add:Address):
        """! Method that allows members to update their delivery address"""
        self.memberAddress = add




if __name__ == '__main__':
    
    # Address
    ad = Address('streeName', 'city', 'postcode')

    # Payment
    py = Payment(100.05)

    # OrderLine list
    olList = []
    p1 = Product(101, 'Retro Skateboard', 20.00, 1)
    ol = OrderLine(p1, 5)
    olList.append(ol) # List[OrderLine]

    # Order list
    oList = []
    time_now = datetime.now()
    o = Order(121, 1, time_now, 20.5, 50, ad, py, olList)
    oList.append(o)

    # shopCart
    pList = []
    pList.append(p1)
    s = ShoppingCart(pList)

    m = Member('会员No.1', 'syc694482337', 'syc@159258', 
                '694482337@qq.com', 'memberNO.1', '1 mountain road',
                '02102212984', s, oList)

    m.getName()
    # m.login('sharon', 'sharon123', flag=2)
    # # 如果代码中临时变量的数据没有存入数据库是不能登录成功的。
    # m.logout('sharon', 2)



    # m.addProduct(p1)
    # m.removeProduct(p1)
    # m.viewCart()
    # m.checkOut()

    # # 下订单: 需要一个orderLine的list、地址、payment
    # # Order list
    # orderData = [ad, py, olList]

    # m.placeOrder(orderData) #下订单

    # time_now = datetime.now()
    # o = Order(121, 1, time_now, 20.5, 50, ad, py, olList)

    # m.viewOrderStatus(o)
    # # o2 = m.getOrder(123)
    # # m.cancelOrder(o2)
    # # m.viewOrders()
    # m.makePayment(o)

    

