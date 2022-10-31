import random
from tkinter import Tk, messagebox
from controller import Controller
from registerUser import RegisteredUser
from order import Order
from datetime import datetime
from address import Address
from payment import Payment
from orderline import OrderLine
from product import Product
from customer import Customer
from guest import Guest
from member import Member
from shoppingcart import ShoppingCart
from creditcard import CreditCard
from bank import Bank

class OnlineShopping():
    def __init__(self) -> None:
        # 初始化所有类别
        # 从文件中读取出来
        self.staffList = self.readGuest()
        self.memberList = self.readMember()
        self.guestList = self.readGuest()
        self.productList = self.readProduct()
        self.cardList = self.readCard()
        self.addList = self.readAddress()
        self.bankList = self.readBank()

        print('This is OnlineShopping class')
    
    def getProductList(self):
        return self.productList
        
    def readStaff(self):
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

    def readMember(self):
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

    def readGuest(self):
        # init
        file = './dataset/Guest.txt'
        guestList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                guestList.append(user)

        return guestList
    
    def readProduct(self):
        # init
        file = './dataset/Product.txt'
        productList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                productList.append(user)

        return productList
    
    def readCard(self):
        # init
        file = './dataset/Card.txt'
        cartList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                cartList.append(user)

        return cartList

    def readBank(self):
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

    def readAddress(self):
        # init
        file = './dataset/Address.txt'
        addressList = []
        with open(file=file, encoding='utf-8') as f:
            for line in f.readlines():
                user = []
                line = line.replace('\n', '').split(',')
                for item in line:
                    item = item.replace(' ', '')
                    user.append(item)
                addressList.append(user)

        return addressList


    def loginInfo(self, username, password, flag):
        # 检查账号密码是否正确无误
        if Controller.login(username, password, flag) == True:
            messagebox.showinfo("Login", username + ' login successful')
            # self指的是GUI
            self.memberMenue()
            return True

        messagebox.showinfo("Login", username + ' login failed!')
        return False

    def logoutInfo(username, flag):
        # 检查账号密码是否正确无误
        if Controller.logout(username, flag) == True:
            messagebox.showinfo("Logout", username + ' logout successful')
            # memberMenue
            return True

        return False
    
    def viewProduct(productList):
        Controller.viewProduct(productList)

    
    

if __name__ == '__main__':
    os = OnlineShopping()
    staff = os.staffList
    member = os.memberList
    guest = os.guestList
    product = os.productList
    card = os.cardList
    address = os.addList

