from controller import Controller
from member import Member
from order import Order
from datetime import datetime
from address import Address
from payment import Payment
from orderline import OrderLine
from product import Product
from customer import Customer
from shoppingcart import ShoppingCart

    
class Guest(Customer):
    """! Guest class, child class of Customer
    Inherits Customer class' attributes and methods
    """
    
    def __init__(self, personName:str, shoppingCart:ShoppingCart):
        super().__init__(personName, shoppingCart)
        """! The class initialiser
        @param personName guests' names
        @param ShoppingCart guests' shopping carts"""
        self.guestName = personName
        self.ShoppingCart = shoppingCart
        print('This Guest class')
    
    def getName(self):
        return super().getName()
    
    

    def addProduct(self, product):
        """! Guests can add products in their shopping carts"""
        # print('add'+ product)
        super().addProduct(product) #插个眼，看看运行效果

    def removeProduct(self, product):
        """! Guests can remove products from their shopping carts"""
        # print('remove' + product)
        super().removeProduct(product) #插个眼，看看运行效果

    def viewCart(self, product):
        """! Guests can view their shopping carts"""
        print('viewCart' + product)
        super().viewCart(product) #插个眼，看看运行效果

    def checkOut(self, gname):
        """! Guests can check out for the products in their shopping carts""" 
        print('非会员不可下单')
        # Address
        ad = Address('streeName', 'city', 'postcode')

        # Payment
        py = Payment(100.05)

        p1 = Product(101, 'Retro Skateboard', 20.00, 1)
        # OrderLine list
        olList = []
        ol = OrderLine(p1, 5)
        olList.append(ol) # List[OrderLine]

        # Order list
        oList = []
        time_now = datetime.now()
        o = Order(121, 1, time_now, 20.5, 50, ad, py, olList)
        oList.append(o)


        # 把转正数据封装到registerDate里面
        registerData = ['yuan', 'yuan123', '694482337@qq.com', 
                        'memberNO.1', '1 mountain road', '02102212984']
        self.register(registerData, oList) # 注册会员

        # 把注册功能摘出来，等待guest选择确认按钮
        # Controller.register(self.guestName, registerData, self.ShoppingCart, oList)
    
    def register(self, data, orderList) -> bool:
        """! Guests can register as member"""
        # gname:guestName用来申请username

        # 注册思路是new一个customer，然后把guess的值赋值过去
        # 注意处理用户list，一个删除，一个添加
        # 简单来说把guest的名字和shoppingCart复制到new成员里面
        Controller.register(data, orderList)

        newMember = Member(self.personName, data[0], data[1], data[2], data[3], data[4], data[5], 
                            self.ShoppingCart, orderList)

        return newMember


if __name__ == '__main__':

    # guest里面需要self， customer需要self， controller不需要self
    # 原因：guset是继承了customer类，二者一脉相传，controller只是引用他的类方法。
    # Address
    ad = Address('streeName', 'city', 'postcode')

    # Payment
    py = Payment(100.05)

    p1 = Product(101, 'Retro Skateboard', 20.00, 1)
    # OrderLine list
    olList = []
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
    sh = ShoppingCart(pList)

    g = Guest('法外狂徒', sh)

    # 把转正数据封装到registerDate里面
    registerData = ['yuan', 'yuan123', '694482337@qq.com', 
                    'memberNO.1', '1 mountain road', '02102212984']

    newG = g.register(registerData, oList )
    print(newG.personName)


