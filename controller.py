# These are the list of methods that you will need for your controller.
# However, these are not exhaustive, you may add more methods as needed.

from order import Order
from creditcard import CreditCard
from bank import Bank
from shoppingcart import ShoppingCart
import os

class Controller:

    def __init__(self):
        self.staffList = self.readGuest()
        self.memberList = self.readMember()
        self.productList = []
        self.categoryList = []
        self.bankList = self.readBank()
        self.cardList = self.readCard()
        print('This is controller class')

    def readBank():
        # init
        file = './dataset/Bank.txt'
        bankList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                bankList.append(user)

        return bankList

    def readCard():
        # init
        file = './dataset/Card.txt'
        cardList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                cardList.append(user)

        return cardList

        
    def readStaff():
        # init
        file = './dataset/Staff.txt'
        staffList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                staffList.append(user)

        return staffList

    def readMember():
        # init
        file = './dataset/Member.txt'
        memberList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    user.append(item)
                memberList.append(user)

        return memberList

    def readGuest():
        # init
        file = './dataset/Guest.txt'
        guestList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    print(item)
                    user.append(item)
                guestList.append(user)

        return guestList
    
    def readOrder(name):
        file = './dataset/Order/'+name+'.txt'

        bankList = []
        with open(file=file, mode='r+', encoding='utf-8') as f:
            for line in f.readlines():
                if len(line) > 0:
                    line = line.replace('\n', '').split(',')
                    # print(line)
                    bankList.append(line)
        return bankList
    
    def readOrderByStaff():
        dir = './dataset/Order/'
        dirList = []
        for filename in os.listdir(dir):
            dirList.append(filename)

        bankList = []
        for path in dirList:
            file = dir + path
            with open(file=file, mode='r+', encoding='utf-8') as f:
                for line in f.readlines():
                    if len(line) > 0:
                        line = line.replace('\n', '').split(',')
                        bankList.append(line)
        return bankList

    def login(username, passwd, flag):
        # 从数据库中核验用户名和密码是否匹配
        if flag == 1:
            # 从staff的数据库中读取
            checkTxt = Controller.readStaff()
        elif flag == 2:
            # 从member的数据库中读取
            checkTxt = Controller.readMember()
        elif flag == 3:
            # 从guest的数据库中读取
            checkTxt = Controller.readGuest()
        elif flag == 4:
            checkTxt = Controller.readCard()
            for item in checkTxt:
                if username == item[0] and passwd == item[1]:
                    return item
        else: #flag=5
            checkTxt = Controller.readBank()
            for item in checkTxt:
                if username == item[0] and passwd == item[1]:
                    return item

        for item in checkTxt:
            if username == item[1] and passwd == item[2]:
                # check it!
                return item

        return None


    def logout(username, flag):
        # 从数据库中核验用户名是否匹配
        if flag == 1:
            # 从staff的数据库中读取
            checkTxt = Controller.readStaff()
        elif flag == 2:
            # 从member的数据库中读取
            checkTxt = Controller.readMember()
        else:
            # 从guest的数据库中读取
            checkTxt = Controller.readGuest()

        for user in checkTxt:
            if username == user[1]:
                # check it!
                return True

        return False

    def viewProduct(productList):
        for item in productList:
            print(item)


    def searchProduct(productList,prodID):
        for item in productList:
            if prodID == item.productID:
                print(item)
                return item


    def searchMember(memberList,memberName):
        for men in memberList:
            if memberName == men.personName:
                print(men)
                return men


    def searchStaff(staffList,staffName):
        for staff in staffList:
            if staffName == staff.personName:
                print(staff)
                return staff

    def searchCategory(productList,catID):
        for item in productList:
            if catID == item.categoryID:
                print(item)
                return item


    def addToCart(product, userShoppingCart):
        # 传入某个人的购物车，controller对这个人的购物车进行操作
        # 返回购物车的长度
        result = userShoppingCart.addItem(product)
        print('Controller.addToCart success')

        return len(userShoppingCart.productList)



    def viewCart(shoppingCart:ShoppingCart):
        # 显示某个用户的cart列表
        # 需要对product重写str方法
        print('Controller.viewCart')
        shoppingCart.listItem()



    def removeFromCart(product, userShoppingCart):
        # 传入某个人的购物车，controller对这个人的购物车进行操作
        # 返回购物车的长度
        result = userShoppingCart.removeItem(product)
        print('Controller.removeFromCart success')

        return len(userShoppingCart.productList)


    def checkOut(shoppingCart):
        shoppingCart.currentTotal()
        print('Controller.checkOut')


    def viewAllOrder(orderList):
        for item in orderList:
            print(item) #order基础属性
            print(item.shippingAddress)
            print(item.paymentDetails)
            for det in item.orderDet:
                print(det)

    def viewOrder(ord:Order):
        print(ord)
        # print('view order successful')


    def cancelOrder(orderList):
        orderList.remove(ord) #加入到当前会员的订单list中


    def makePayment(ordDet:Order):
        # 支付之前
        needPay = ordDet.paymentDetails.paymentAmt
        print('当前账单需要支付的金额：{}'.format(needPay))

        choice = input('选择支付方式:CreditCard(0) or Bank(1)')
        if choice == '0':
            payId = input('输入卡号: ')
            payType = input('输入卡的类型:visa or mastercard: ')
            card = CreditCard(needPay, payId, payType)
            print('支付成功')
        elif choice == '1':
            bankId = input('输入银行账号: ')
            bankName = input('输入银行名字: ')
            bank = Bank(needPay, bankId, bankName)
            print('支付成功')

        # 支付之后
        ordDet.updatePayment(ordDet.paymentDetails)
        needPay = ordDet.paymentDetails.paymentAmt
        print('当前账单需要支付的金额：{}'.format(needPay))


    def generateReport(self, sname):
        # staff
        pass

    