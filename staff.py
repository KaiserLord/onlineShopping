from registerUser import RegisteredUser
from order import Order
from datetime import datetime
from address import Address
from payment import Payment
from orderline import OrderLine
from product import Product

class Staff(RegisteredUser):
    """! Staff class, child class of Class RegisteredUser
    Inherits parent class attributes and methods
    Staff can view customers orders, generate reports and update customers' orders"""

    def __init__(self, personName:str, username:str, password:str, 
                email:str,staffID:str,staffPosition:str,OrderList:list):
        RegisteredUser.__init__(self, personName, username, password, email)
        """! The class initialiser
        @param personName staff names
        @param username staff login user names
        @param password staff login password
        @param email staff emails
        @param staffID staff ID
        @param staffPosition staff positions
        @param OrderList order lists
        """
        self.personName = personName
        self.username = username
        self.password = password
        self.email = email
        self.staffID = staffID
        self.staffPosition = staffPosition
        self.orderList = OrderList



    def getName(self):
        """! Get staff names"""
        print(self.personName)
        return self.getName

    def login(self,username, password, flag):
        """! login method allows staff to login
        @param username usernames for staff to login
        @param password password that staff can use to login
        """
        RegisteredUser.login(self, username, password, flag)
    
    def logout(self, username, flag):
        """! logout method allows staff to log out of the system"""
        RegisteredUser.logout(self, username, flag)

    
    def ViewOrders():
        """! Staff can view customers' orders in the order history tab"""
        
        pass
    
    def generateReport():
        """! Staff can generate reports"""
        pass

    def updateOrder():
        """! Staff can update customers' orders where needed"""
        pass

if __name__=='__main__':

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

    s = Staff('员工No.1', 'syc694482337', 'syc@159258', 
                '694482337@qq.com', 'staffNO.1', 
                'CEO', oList)
    s.login('sharon', 'sharon123', flag=2)
    # 如果代码中临时变量的数据没有存入数据库是不能登录成功的。
    s.logout('sharon', 1)

