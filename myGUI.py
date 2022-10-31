from datetime import datetime
from email import message
import os
import random
from tkinter import *
import tkinter
from tkinter import scrolledtext
from address import Address
from guest import Guest
from member import Member
from onlineshopping import OnlineShopping
from tkinter import messagebox
from controller  import Controller
from order import Order
from orderline import OrderLine
from payment import Payment
from product import Product
from shoppingcart import ShoppingCart
from collections import Counter

from staff import Staff

class myGUI():
    def __init__(self, onlineshop) -> None:
        self.scrolW = 100
        self.scrolH = 300
        self.shop = onlineshop
        self.staffs = onlineshop.staffList
        self.members = onlineshop.memberList
        self.guests = onlineshop.guestList
        self.products = onlineshop.productList
        self.cards = onlineshop.cardList
        self.addresses = onlineshop.addList
        self.bank = onlineshop.bankList
        self.ordId = 1
    
    def show(self):
        top = Tk()
        top.title('online shopping')
        top.geometry('700x700')

        button1 = Button(top, text='login', width=10, height=1, 
                        command=None)
        button1.place(x=250, y=170)

        button2 = Button(top, text='guest', width=10, height=1, 
                        command=None)
        button2.place(x=350, y=170)

        top.mainloop()



    def loginInterface(self):
        def goto(num):
            root.destroy() # 关闭主窗体
            if num==1:            
                self.member() # 进入第1个窗体
            elif num==2:
                self.guest() # 进入第2个窗体
            elif num==3:
                self.staff() # 进入第3个窗体
        
        root=Tk()
        root.geometry('700x700')
        root.title('主界面：欢迎来到登陆界面')
        but1=Button(root,text="member",width=10, height=1, command=lambda:goto(1)) # 进入窗口1
        but1.pack(pady=10)
        but2=Button(root,text="guest",width=10, height=1, command=lambda:goto(2)) # 进入窗口2
        but2.pack(pady=10)
        but3=Button(root,text="staff",width=10, height=1, command=lambda:goto(3)) # 进入窗口3
        but3.pack(pady=10)
    
        root.mainloop() 
    
    
    def addProduct(self, prod, prodInfo, user):
        
        p_choose = prod.get(SEL_FIRST,SEL_LAST) #商品框
        for memItem in self.products: 
            if memItem[0] == p_choose:
                memIndex = self.products.index(memItem) #记下mem索引
        item = self.products[memIndex]
        print(item)
        if item not in user.ShoppingCart.productList:
            user.addProduct(item) #add to user's shopping cart
        else: 
            for it in user.ShoppingCart.productList:
                if it[0] == item[0]:
                    # don't add to shoppingcart
                    it[5] = int(it[5]) + 1

        # prodInfo.insert('end', item) #购物车框

        pritprodDesc = item[1]
        pritprodPrice = str(item[2])
        pritCateId = item[3]
        pritCateDesc = item[4]
        
        prodInfo.insert('end', str(item[0]) + ' ')
        prodInfo.insert('end', pritprodDesc.ljust(30, ' '))
        prodInfo.insert('end', pritprodPrice.ljust(15, ' '))
        prodInfo.insert('end', pritCateId.ljust(10, ' '))
        prodInfo.insert('end', pritCateDesc.ljust(10, ' '))
        prodInfo.insert('end', str(item[5]))
        prodInfo.insert('end', '\n')


    def removeProduct(self, prodInfo, user):
        p_choose = prodInfo.get(SEL_FIRST,SEL_LAST)
        print(p_choose)
        prodInfo.delete(1.0, END) #clear
        pList = user.ShoppingCart.productList
        for item in pList:
            if item[0] == p_choose:
                if int(item[5]) > 1:
                    item[5] = int(item[5]) - 1
                else:
                    user.removeProduct(item)
                    print('remove ok')
        
        user.ShoppingCart.productList = pList
        for item in user.ShoppingCart.productList:
            prodInfo.insert('end', item) #购物车框
            prodInfo.insert('end', '\n')



    def emptyProduct(self, prodInfo):
        prodInfo.delete(1.0, END)
        print('clear ok')

    def findProduct(self, prodFindEntry, searchRes):
        
        pid = prodFindEntry.get()
        pIndex = 0
        for pItem in self.products: 
            if pItem[0] == pid:
                pIndex = self.products.index(pItem) #记下mem索引
        item = self.products[pIndex]

        searchRes.insert('end', item) #购物车框
        searchRes.insert('end', '\n')


    def checkCard(self, root1, cardNumber, cardType, ord):

        # 检查账号密码是否正确无误
        result = Controller.login(cardNumber, cardType, flag=4)
        if result == None:
            messagebox.showinfo('Card', "checkout failed!")
            return None
        # login successful
        messagebox.showinfo('Card', "checkout success, thank you for you visting")
        ord.orderStatus = 1 #'awaiting shipment'

        root1.destroy()
        self.loginInterface()

    def creditCard(self, root1, user, ord):
        # 验证输入的card信息
        # 确认支付
        # 弹窗:支付成功
        root1.destroy() # 关闭第1个窗体

        top = Tk()
        top.title('Credit card')
        top.geometry('700x700')

        Label(top, text='cardNumber:').place(x=100, y=200)
        Label(top, text='card  Type:').place(x=100, y=250)

        # Id number
        cardNumber = StringVar()
        entry_card_id = Entry(top, textvariable=cardNumber)
        entry_card_id.place(x=200, y=200)

        # type
        cardType = StringVar()
        entry_card_type = Entry(top, textvariable=cardType)
        entry_card_type.place(x=200, y=250)

        but = Button(top, text='确认', width=10, height=1, command=lambda:self.checkCard(top, entry_card_id.get(), entry_card_type.get(), ord))
        but.place(x=250, y=300)

        top.mainloop()

    def checkBank(self, root1, bankNumber, bankType, ord):

        # 检查账号密码是否正确无误
        print(type(bankNumber))
        result = Controller.login(bankNumber, bankType, flag=5)
        if result == None:
            messagebox.showinfo('Bank', "checkout failed!")
            return None
        # login successful
        messagebox.showinfo('Bank', "checkout success, thank you for you visting")
        ord.orderStatus = 1 #'awaiting shipment'

        root1.destroy()
        self.loginInterface()

    def bankPay(self, root1, user, ord):
        # 验证输入的bank信息
        # 确认支付
        # 弹窗:支付成功
        root1.destroy() # 关闭第1个窗体

        top = Tk()
        top.title('Bank')
        top.geometry('700x700')

        Label(top, text='bankNumber:').place(x=100, y=200)
        Label(top, text='bank  Type:').place(x=100, y=250)

        # Id number
        bankNumber = StringVar()
        entry_bank_id = Entry(top, textvariable=bankNumber)
        entry_bank_id.place(x=200, y=200)

        # type
        bankType = StringVar()
        entry_bank_type = Entry(top, textvariable=bankType)
        entry_bank_type.place(x=200, y=250)

        but = Button(top, text='确认', width=10, height=1, command=lambda:self.checkBank(top, entry_bank_id.get(), entry_bank_type.get(), ord))
        but.place(x=250, y=300)

        top.mainloop()

    def makePayment(self, root1, user, ord):
        root1.destroy() # 关闭第1个窗体
        top = Tk()
        top.title('make payment')
        top.geometry('700x700')

            
        # show info
        label1= Label(top,text= user.getName() + " payment")
        label1.place(x=100, y=120)
        showOrder = scrolledtext.ScrolledText(top, width=80, height=10)
        showOrder.place(x=100, y=150)

        pList = user.ShoppingCart.productList
        for item in pList:
            pritprodDesc = 'prodDesc: '+item[1]
            pritprodPrice = 'prodPrice: ' + item[2]
            
            showOrder.insert('end', 'prodID: '+item[0] + ' ')
            showOrder.insert('end', pritprodDesc.ljust(30, ' '))
            showOrder.insert('end', pritprodPrice.ljust(15, ' '))
            showOrder.insert('end', 'prodQty: ' + str(item[5]))
            showOrder.insert('end', '\n')
            
        showOrder.insert('end', 'Total cost is : ' + str(ord.paymentDetails.paymentAmt))


        # 选择支付方式
        button1 = Button(top, text='CreditCard', width=10, height=1, command=lambda:self.creditCard(top, user, ord))
        button1.place(x=250, y=300)

        button2 = Button(top, text='Bank', width=10, height=1, command=lambda:self.bankPay(top, user, ord))
        button2.place(x=350, y=300)

        top.mainloop()

    def makeOrder(self, root1, user):
        root1.destroy() # 关闭第1个窗体
        top = Tk()
        top.title('make order')
        top.geometry('700x700')
            
        
        label1= Label(top,text= user.getName() + " order")
        label1.place(x=100, y=120)
        showOrder = scrolledtext.ScrolledText(top, width=70, height=10)
        showOrder.place(x=100, y=150)

        # total
        amt = 0.0
        ordAdd = user.getAddress()
        ordDet = []
        pList = user.ShoppingCart.productList
        for item2 in pList:
            print(item2)
            amt += (float(item2[2]) * float(item2[5]))
            p = p = Product(int(item2[0]), item2[1], float(item2[2]), int(item2[3]), item2[4], int(item2[5]))
            ordLine = OrderLine(p, int(item2[5]))
            ordDet.append(ordLine)
        
        # create order obj
        shipCost = random.randint(1,10)
        ordPay = Payment(amt + shipCost)
        time_now = datetime.now()
        status = 0
        ordId = time_now.microsecond
        ord = Order(ordId, status, time_now, amt, shipCost, ordAdd, ordPay, ordDet) #0：processing
        user.orderList.append(ord) #add to member
        tempOrd = user.orderList #查看订单数量
        print(user.orderList.index(ord))
        print(len(tempOrd))

        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})
        showOrder.insert('end', 'orderId: '+str(ordId) + ' ')
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'orderStatus: '+ordStatus[status]+ ' ')
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'orderDate: ')
        showOrder.insert('end', time_now)
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'orderTotal: '+str(amt) + ' ')
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'shippingCost: '+ str(shipCost) + ' ')
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'shippingAddress: '+ordAdd.getAddress() + ' ')
        showOrder.insert('end', '\n')
        showOrder.insert('end', 'paymentDetails: '+str(ordPay.paymentAmt) + ' ')
        showOrder.insert('end', '\n')

                
        for ordItem in tempOrd:
            for item in ordItem.orderDet:
                showOrder.insert('end', '\n----------------------------------\n')
                showOrder.insert('end', 'orderLine productId: '+ str(item.product.productID) + ' ')
                showOrder.insert('end', '\n')
                showOrder.insert('end', 'orderLine productDesc: '+ str(item.product.productDescription) + ' ')
                showOrder.insert('end', '\n')
                showOrder.insert('end', 'orderLine price: '+ str(item.product.price) + ' ')
                showOrder.insert('end', '\n')
                showOrder.insert('end', 'orderLine qty: '+ str(item.qty) + ' ')

        
        # restore order to file
        self.restoreOrd(user)

        button1 = Button(top, text='cancel', width=10, height=1, command=lambda:self.memberMenue(user, top))
        button1.place(x=100, y=300)

        button2 = Button(top, text='payment', width=10, height=1, command=lambda:self.makePayment(top, user, ord))
        button2.place(x=200, y=300)

        button3 = Button(top, text='update address', width=20, height=1, command=lambda:self.updateAddress(top, user, ord))
        button3.place(x=300, y=300)

        top.mainloop()

    def updateAddress(self, root1, user, ord):
        root1.destroy()
        root = Tk()
        root.geometry('700x700')
        root.title('welcome member')

        Label(root, text='streeName:').place(x=100, y=100)
        Label(root, text='city      :').place(x=100, y=140)
        Label(root, text='postcode  :').place(x=100, y=180)

        temp = StringVar()
        streeName = Entry(root, textvariable=temp)
        streeName.place(x=180, y=100)

        temp1 = StringVar()
        city = Entry(root, textvariable=temp1)
        city.place(x=180, y=140)

        temp2 = StringVar()
        postcode = Entry(root, textvariable=temp2)
        postcode.place(x=180, y=180)

        but = Button(root, text='Update', width=10, height=1, command=lambda:self.addressTemp(root, streeName.get(), city.get(), postcode.get(), user, ord))
        but.place(x=350, y=450)

        root.mainloop()

    def addressTemp(self, root1, sName, city, pcode, user, ord):
        address = ord.shippingAddress
        index = user.orderList.index(ord)
        address.streeName = sName
        address.city = city
        address.postcode = pcode
        user.orderList[index] = ord
        messagebox.showinfo('update address', 'update shipping address successful')

        self.memberMenue(user, root1)




        

    def memberMenue(self, memberUser, root1):
        def gotomain():
            root.destroy() # 关闭第1个窗体
            self.loginInterface() # 返回主窗体clear

        root1.destroy()
        root = Tk()
        root.geometry('900x700')
        root.title('welcome member')

        # products
        label1= Label(root,text="products")
        label1.place(x=100, y=29)
        prod = scrolledtext.ScrolledText(root, width=100, height=10)
        prod.place(x=100, y=50)
        
        # show search result
        label2= Label(root,text= 'show search result')
        label2.place(x=100, y=220)
        searchRes = scrolledtext.ScrolledText(root, width=100, height=10)
        searchRes.place(x=100, y=250)

        # search product
        prodFindEntry = Entry(root)
        prodFindEntry.place(x=200, y=15)
        prodFindBut = Button(root, text='search product by id', width=20, height=1, command=lambda:self.findProduct(prodFindEntry, searchRes))
        prodFindBut.place(x=400, y=10)
        emptyFind = Button(root, text='empty', width=10, height=1, command=lambda:self.emptyProduct(searchRes))
        emptyFind.place(x=600, y=390)
        

        # show all products
        productList = self.products
        for item in productList:
            # print(item)
            pritprodDesc = 'prodDesc: '+item[1]
            pritprodPrice = 'prodPrice: ' + item[2]
            pritCateId = 'cateID: '+item[3]
            pritCateDesc = 'cateDesc: '+item[4]
            
            prod.insert('end', 'prodID: '+item[0] + ' ')
            prod.insert('end', pritprodDesc.ljust(30, ' '))
            prod.insert('end', pritprodPrice.ljust(15, ' '))
            prod.insert('end', pritCateId.ljust(10, ' '))
            prod.insert('end', pritCateDesc.ljust(10, ' '))
            prod.insert('end', '\n')


        # memberUser's shoppingcart:
        label3= Label(root,text= memberUser.getName() + " shoppingcart")
        label3.place(x=100, y=420)
        shopping = scrolledtext.ScrolledText(root, width=100, height=10)
        shopping.place(x=100, y=450)
        for preItem in memberUser.ShoppingCart.productList:
            pritprodDesc = preItem[1]
            pritprodPrice = str(preItem[2])
            pritCateId = preItem[3]
            pritCateDesc = preItem[4]
            
            shopping.insert('end', str(preItem[0]) + ' ')
            shopping.insert('end', pritprodDesc.ljust(30, ' '))
            shopping.insert('end', pritprodPrice.ljust(15, ' '))
            shopping.insert('end', pritCateId.ljust(10, ' '))
            shopping.insert('end', pritCateDesc.ljust(10, ' '))
            shopping.insert('end', str(preItem[5]))
            shopping.insert('end', '\n')



        #add & remove & empty
        # Detail button:根据鼠标选中的名字，在文本框显示详情
        button1 = Button(root, text='add', width=10, height=1, command=lambda:self.addProduct(prod, shopping, memberUser))
        button1.place(x=100, y=600)

        button2 = Button(root, text='remove', width=10, height=1, command=lambda:self.removeProduct(shopping, memberUser))
        button2.place(x=200, y=600)

        button3 = Button(root, text='empty', width=10, height=1, command=lambda:self.emptyProduct(shopping))
        button3.place(x=300, y=600)

        button4 = Button(root, text='make order', width=20, height=1, command=lambda:self.makeOrder(root, memberUser))
        button4.place(x=400, y=600)

        button4 = Button(root, text='order history', width=20, height=1, command=lambda:self.orderHistory(root, memberUser))
        button4.place(x=600, y=600)

        but = Button(root, text="return to main interface",command=gotomain)
        but.place(x=600, y=10)

        root.mainloop()


    def orderHistory(self, root1, memberUser):
        #only show thsi menber's order
        root1.destroy()
        root = Tk()
        root.geometry('900x700')
        root.title('welcome member')

        label1= Label(root,text="history orders")
        label1.place(x=100, y=29)

        prod = scrolledtext.ScrolledText(root, width=100, height=30)
        prod.place(x=100, y=50)
        
        label2= Label(root,text= 'cancel order')
        label2.place(x=100, y=480)
        cancelText = scrolledtext.ScrolledText(root, width=100, height=10)
        cancelText.place(x=100, y=500)

        temp = StringVar()
        cancelEntry = Entry(root, textvariable=temp)
        cancelEntry.place(x=200, y=470)


        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})

        if len(memberUser.orderList) == 0:
            # 新用户
            messagebox.showinfo('order history', '新用户没有订单记录')
            self.memberMenue(memberUser, root)
        
        else:
            # 老用户
            for item in memberUser.orderList:
                print(type(item))
                
                prod.insert('end', 'orderId: '+str(item.orderID) + ' ')
                prod.insert('end', '\n')
                prod.insert('end', 'orderStatus: '+ordStatus[item.orderStatus]+ ' ')
                prod.insert('end', '\n')
                prod.insert('end', 'orderDate: ')
                prod.insert('end', item.orderDate)
                prod.insert('end', '\n')
                prod.insert('end', 'orderTotal: '+str(item.orderTotal) + ' ')
                prod.insert('end', '\n')
                prod.insert('end', 'shippingCost: '+ str(item.shippingCost) + ' ')
                prod.insert('end', '\n')
                prod.insert('end', 'shippingAddress: '+item.shippingAddress.getAddress() + ' ')
                prod.insert('end', '\n')
                prod.insert('end', 'paymentDetails: '+str(item.paymentDetails.paymentAmt) + ' ')
                prod.insert('end', '\n\n')

        button1 = Button(root, text='cancel', width=20, height=1, command=lambda:self.cancelOrder(memberUser, cancelEntry.get(), cancelText))
        button1.place(x=400, y=650)


        but = Button(root, text="return to member menue",command=lambda:self.memberMenue(memberUser, root))
        but.place(x=600, y=650)

        root.mainloop()


    def cancelOrder(self, user, celOrd, cancelText):
        
        orderList = user.orderList
        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})
        for ord in orderList:
            if ord.orderID == int(celOrd):
                if ord.orderStatus < 2:
                    # 可以取消订单
                    orderList.remove(ord)
                    messagebox.showinfo('cancel order', 'This order is canceled!')
                    cancelText.delete(1.0, END)

                    for item in orderList:
                        cancelText.insert('end', 'orderId: '+str(item.orderID) + ' ')
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'orderStatus: '+ordStatus[item.orderStatus]+ ' ')
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'orderDate: ')
                        cancelText.insert('end', item.orderDate)
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'orderTotal: '+str(item.orderTotal) + ' ')
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'shippingCost: '+ str(item.shippingCost) + ' ')
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'shippingAddress: '+item.shippingAddress.getAddress() + ' ')
                        cancelText.insert('end', '\n')
                        cancelText.insert('end', 'paymentDetails: '+str(item.paymentDetails.paymentAmt) + ' ')
                        cancelText.insert('end', '\n\n')
                else:
                    # 不可取消
                    messagebox.showinfo('cancel order', 'This order can not cancel!')

        user.orderList = orderList
        # self.restoreOrd(user)

    def findOrder(self, orderList, ordFindEntry, searchRes):
        pid = ordFindEntry.get()
        pIndex = 0
        for ordItem in orderList: 
            print(type(ordItem.orderID))
            print(type(pid))
            if ordItem.orderID == int(pid):
                pIndex = orderList.index(ordItem) #记下mem索引

        item = orderList[pIndex]
        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})
        searchRes.insert('end', 'orderId: '+str(item.orderID) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderStatus: '+ordStatus[item.orderStatus]+ ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderDate: ')
        searchRes.insert('end', item.orderDate)
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderTotal: '+str(item.orderTotal) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'shippingCost: '+ str(item.shippingCost) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'shippingAddress: '+item.shippingAddress.getAddress() + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'paymentDetails: '+str(item.paymentDetails.paymentAmt) + ' ')
        searchRes.insert('end', '\n')

        for item in item.orderDet:
            if isinstance(item, list):
                # list中含有多个orderline
                for olk in item:
                    searchRes.insert('end', '\n----------------------------------\n')
                    searchRes.insert('end', 'orderLine productId: '+ str(olk.product.productID) + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine productDesc: '+ olk.product.productDescription + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine price: '+ str(olk.product.price) + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine qty: '+ str(olk.qty) + ' ')
                    searchRes.insert('end', '\n\n')
            else:
                # item就是orderline实体
                searchRes.insert('end', '\n----------------------------------\n')
                searchRes.insert('end', 'orderLine productId: '+ str(item.product.productID) + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine productDesc: '+ item.product.productDescription + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine price: '+ str(item.product.price) + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine qty: '+ str(item.qty) + ' ')
                searchRes.insert('end', '\n\n')
        print('findOrder')


    def emptyOrder(self, searchRes):
        print('emptyOrder')
        searchRes.delete(1.0, END)

    
    def updateOrder(self, user, searchRes, modEntry, root1):
        # 要更改的订单必须先索引出来：从搜索框中选择要update的订单
        # order状态只能从0状态转变为1状态，不可以跳跃转变状态，这样更加符合实际
        # 更新状态后的order，同样在搜索结果展示框显示。
        ordId = modEntry.get()
        searchRes.delete(1.0, END)
        orderList = user.orderList
        pIndex = 0
        for ordItem in orderList: 
            if ordItem.orderID == int(ordId):
                if ordItem.orderStatus < 3: #订单未结束
                    ordItem.orderStatus += 1
                    pIndex = orderList.index(ordItem) #记下mem索引
                else:
                    messagebox.showwarning('update order', '当前订单已完结,不可更改其状态!')
                    self.staffMenue(user, root1)


        item = orderList[pIndex]
        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})
        searchRes.insert('end', 'orderId: '+str(item.orderID) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderStatus: '+ordStatus[item.orderStatus]+ ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderDate: ')
        searchRes.insert('end', item.orderDate)
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'orderTotal: '+str(item.orderTotal) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'shippingCost: '+ str(item.shippingCost) + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'shippingAddress: '+item.shippingAddress.getAddress() + ' ')
        searchRes.insert('end', '\n')
        searchRes.insert('end', 'paymentDetails: '+str(item.paymentDetails.paymentAmt) + ' ')
        searchRes.insert('end', '\n')

        for item in item.orderDet:
            if isinstance(item, list):
                # list中含有多个orderline
                for olk in item:
                    searchRes.insert('end', '\n----------------------------------\n')
                    searchRes.insert('end', 'orderLine productId: '+ str(olk.product.productID) + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine productDesc: '+ olk.product.productDescription + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine price: '+ str(olk.product.price) + ' ')
                    searchRes.insert('end', '\n')
                    searchRes.insert('end', 'orderLine qty: '+ str(olk.qty) + ' ')
                    searchRes.insert('end', '\n\n')
            else:
                # item就是orderline实体
                searchRes.insert('end', '\n----------------------------------\n')
                searchRes.insert('end', 'orderLine productId: '+ str(item.product.productID) + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine productDesc: '+ item.product.productDescription + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine price: '+ str(item.product.price) + ' ')
                searchRes.insert('end', '\n')
                searchRes.insert('end', 'orderLine qty: '+ str(item.qty) + ' ')
                searchRes.insert('end', '\n\n')

        # 在TXT文件中把对应的order状态更改一下:清空+重写
        # get order master
        file = './dataset/Order.txt'
        ordMasterList = []
        with open(file, 'r+', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.replace('\n', '').split(',')
                ordMasterList.append(line[-1])

        i = 0
        write_p = open(file=file, mode='w', encoding='utf-8')
        
        for ord in orderList:
            ordMaster = ordMasterList[i]
            write_p.writelines([str(ord.orderID)+',', str(ord.orderStatus)+',', str(ord.orderDate)+',', str(ord.orderTotal)+',', str(ord.shippingCost)+',', ord.shippingAddress.streeName+',', ord.shippingAddress.city+',', ord.shippingAddress.postcode+',', str(ord.paymentDetails.paymentAmt)])
        
            for itemDet in ord.orderDet:
                write_p.writelines([','+str(itemDet.product.productID)+',', itemDet.product.productDescription+',', str(itemDet.product.price)+',', str(itemDet.product.categoryID)+',', itemDet.product.categoryDesc+',', str(itemDet.qty)])

            write_p.writelines(','+ordMaster)
            write_p.writelines('\n')
            i += 1

        write_p.close()
    

    def staffMenue(self, user,root1):
        def gotomain():
            root.destroy() # 关闭第1个窗体
            self.loginInterface() # 返回主窗体clear

        root1.destroy()
        root = Tk()
        root.geometry('900x900')
        root.title('welcome staff')

        # orders
        label1= Label(root,text="orders")
        label1.place(x=100, y=29)
        prod = scrolledtext.ScrolledText(root, width=100, height=40)
        prod.place(x=100, y=50)
        
        # show search result
        label2= Label(root,text= 'show search result')
        label2.place(x=100, y=600)
        searchRes = scrolledtext.ScrolledText(root, width=100, height=15)
        searchRes.place(x=100, y=620)

        # search order
        ordFindEntry = Entry(root)
        ordFindEntry.place(x=200, y=15)
        prodFindBut = Button(root, text='search order by id', width=20, height=1, command=lambda:self.findOrder(user.orderList, ordFindEntry, searchRes))
        prodFindBut.place(x=400, y=10)
        emptyBut = Button(root, text='empty', width=10, height=1, command=lambda:self.emptyOrder(searchRes))
        emptyBut.place(x=800, y=850)
        

        # show all orders:user-->orderList-->order obj
        ordStatus = dict({0:'processing', 1:'awaiting shipment', 2:'shipped', 3:'delivered'})
        orderObjs = user.orderList
        for obj in orderObjs:
            
            # obj就是order实体
            prod.insert('end', 'orderId: '+str(obj.orderID) + ' ')
            prod.insert('end', '\n')
            prod.insert('end', 'orderStatus: '+ordStatus[obj.orderStatus]+ ' ')
            prod.insert('end', '\n')
            prod.insert('end', 'orderDate: ')
            prod.insert('end', obj.orderDate)
            prod.insert('end', '\n')
            prod.insert('end', 'orderTotal: '+str(obj.orderTotal) + ' ')
            prod.insert('end', '\n')
            prod.insert('end', 'shippingCost: '+ str(obj.shippingCost) + ' ')
            prod.insert('end', '\n')
            prod.insert('end', 'shippingAddress: '+obj.shippingAddress.getAddress() + ' ')
            prod.insert('end', '\n')
            prod.insert('end', 'paymentDetails: '+str(obj.paymentDetails.paymentAmt) + ' ')
            prod.insert('end', '\n')

            for item in obj.orderDet:
                if isinstance(item, list):
                    # list中含有多个orderline
                    for olk in item:
                        prod.insert('end', '\n----------------------------------\n')
                        prod.insert('end', 'orderLine productId: '+ str(olk.product.productID) + ' ')
                        prod.insert('end', '\n')
                        prod.insert('end', 'orderLine productDesc: '+ olk.product.productDescription + ' ')
                        prod.insert('end', '\n')
                        prod.insert('end', 'orderLine price: '+ str(olk.product.price) + ' ')
                        prod.insert('end', '\n')
                        prod.insert('end', 'orderLine qty: '+ str(olk.qty) + ' ')
                        prod.insert('end', '\n\n')
                else:
                    # item就是orderline实体
                    prod.insert('end', '\n----------------------------------\n')
                    prod.insert('end', 'orderLine productId: '+ str(item.product.productID) + ' ')
                    prod.insert('end', '\n')
                    prod.insert('end', 'orderLine productDesc: '+ item.product.productDescription + ' ')
                    prod.insert('end', '\n')
                    prod.insert('end', 'orderLine price: '+ str(item.product.price) + ' ')
                    prod.insert('end', '\n')
                    prod.insert('end', 'orderLine qty: '+ str(item.qty) + ' ')
                    prod.insert('end', '\n\n')

        #add & remove & empty
        # Detail button:根据鼠标选中的名字，在文本框显示详情

        modOrd = StringVar()
        modEntry = Entry(root, textvariable=modOrd)
        modEntry.place(x=100, y=855)
        button1 = Button(root, text='update order', width=20, height=1, command=lambda:self.updateOrder(user, searchRes, modEntry, root))
        button1.place(x=280, y=850)

        but = Button(root, text="generate report",command=lambda:self.generateReport(user, root))
        but.place(x=500, y=850)

        but = Button(root, text="return to main interface",command=gotomain)
        but.place(x=600, y=10)
        root.mainloop()


    def generateReport(self, user, root1):

        root1.destroy()
        root = Tk()
        root.geometry('900x900')
        root.title('welcome staff')

        # orders
        label1= Label(root,text="Reports")
        label1.place(x=100, y=29)
        prod = scrolledtext.ScrolledText(root, width=80, height=30)
        prod.place(x=100, y=50)

        # addressing data

        dir = './dataset/Order/'
        dirList = []
        for filename in os.listdir(dir):
            dirList.append(filename)

        repoList = []
        for path in dirList:
            file = dir + path
            repo = []

            f = open(file, mode='r+', encoding='utf-8')
            flines = f.readlines()
            ord_num = len(flines)
            ord_money = 0.0
            ord_month = 10
            name = ''
            for line in flines:
                line = line.replace('\n', '').split(',')
                name = line[-1]
                ord_month = line[2].split('-')[1] #month
                ord_money =  ord_money + float(line[8])# monty
                    
            repo.append(name)
            repo.append(ord_num)
            repo.append(ord_money)
            repo.append(ord_month)
            repoList.append(repo)

        # insert to prod
        prod.insert('end', 'Name'.ljust(10, ' '))
        prod.insert('end', 'orderNumber'.ljust(15, ' '))
        prod.insert('end', 'totalMoney'.ljust(15, ' '))
        prod.insert('end', 'month'.ljust(10, ' '))
        prod.insert('end', '\n')
        for showItem in repoList:
            prod.insert('end', showItem[0].ljust(10, ' '))
            prod.insert('end', str(showItem[1]).ljust(20, ' '))
            prod.insert('end', str(showItem[2]).ljust(10, ' '))
            prod.insert('end', str(showItem[3]).ljust(10, ' '))
            prod.insert('end', '\n')

        but = Button(root, text="Return To Staff Menue",command=lambda:self.staffMenue(user, root))
        but.place(x=600, y=10)

        root.mainloop()

    def restoreOrd(self, user):
        # restore order to file
        uName = user.getName()
        file = './dataset/'+uName+'.txt'
        ordMaster = user.getName()
        write_p = open(file=file, mode='w+', encoding='utf-8')

        ordList = user.orderList
        for ord in ordList:
            print(type(ord))
            write_p.writelines([str(ord.orderID)+',', str(ord.orderStatus)+',', str(ord.orderDate)+',', str(ord.orderTotal)+',', str(ord.shippingCost)+',', ord.shippingAddress.streeName+',', ord.shippingAddress.city+',', ord.shippingAddress.postcode+',', str(ord.paymentDetails.paymentAmt)])
            for item in ord.orderDet:
                print(type(item))
                print(type(item.product))
                write_p.writelines([','+str(item.product.productID)+',', item.product.productDescription+',', str(item.product.price)+',', str(item.product.categoryID)+',', item.product.categoryDesc+',', str(item.qty)])

            write_p.writelines(','+ordMaster)
            write_p.writelines('\n')

        write_p.close()


    def loginInfo(self, username, password, flag, root1):
        # 检查账号密码是否正确无误
        result = Controller.login(username, password, flag)
        if result == None:
            messagebox.showinfo("Login", username + ' login failed!')
            return None
        # login successful
        messagebox.showinfo("Login", username + ' login successful')
        
        
        if flag == 2:
            # member
            olList = Controller.readOrder(username)

            userShopping = ShoppingCart([])
            userAddress = Address(result[5], result[6], result[7])
            userOL = [] #load Order from file
            print(type(olList))
            print(olList)
            
            m = 9
            k = 6

            for item1 in olList:
                if item1[-1] == result[1]:
                    ordDet = []
                    temp = (len(item1)-10) / 6
                    if temp > 1: 
                        #该订单还有多个product
                        for i in range(0, int(temp)):
                            p = Product(item1[m+k*i], item1[m+k*i+1], item1[m+k*i+2], item1[m+k*i+3], item1[m+k*i+4], item1[m+k*i+5])
                            oline = OrderLine(p, item1[m+k*i+5])
                            ordDet.append(oline)

                    else:
                        # 单个product的订单
                        p = Product(item1[m], item1[m+1], item1[m+2], item1[m+3], item1[m+4], item1[m+5])
                        oline = OrderLine(p, int(item1[m+5]))
                        ordDet.append(oline)

                    address = Address(item1[5], item1[6], item1[7])
                    paymt = Payment(float(item1[8]))
                    ord = Order(int(item1[0]), int(item1[1]), item1[2], float(item1[3]), float(item1[4]), address, paymt, ordDet)
                    userOL.append(ord)

            user = Member(result[0], result[1], result[2], result[3], result[4], userAddress, result[8], userShopping, userOL)
            self.memberMenue(user,root1)
        
        elif flag == 1:
            # staff
            userOL = [] #load Order from file
            olList = Controller.readOrderByStaff()

            print(type(olList))
            print(olList)
            
            m = 9
            k = 6

            for item1 in olList:
                ordDet = []
                temp = (len(item1)-10) / 6
                if temp > 1: 
                    #该订单还有多个product
                    # ol = []
                    for i in range(0, int(temp)):
                        p = Product(item1[m+k*i], item1[m+k*i+1], item1[m+k*i+2], item1[m+k*i+3], item1[m+k*i+4], item1[m+k*i+5])
                        oline = OrderLine(p, item1[m+k*i+5])
                        # ol.append(oline)
                        ordDet.append(oline)

                else:
                    # 单个product的订单
                    p = Product(item1[m], item1[m+1], item1[m+2], item1[m+3], item1[m+4], item1[m+5])
                    oline = OrderLine(p, int(item1[m+5]))
                    ordDet.append(oline)

                address = Address(item1[5], item1[6], item1[7])
                paymt = Payment(float(item1[8]))
                ord = Order(int(item1[0]), int(item1[1]), item1[2], float(item1[3]), float(item1[4]), address, paymt, ordDet)
                userOL.append(ord)
                
            user = Staff(result[0], result[1], result[2], result[3], result[4], result[5], userOL)
            self.staffMenue(user,root1)


    def logoutInfo(self, username, flag):
        # 检查账号密码是否正确无误
        if Controller.logout(username, flag) == True:
            messagebox.showinfo("Logout", username + ' logout successful')
            # memberMenue
            return True

        return False

    def member(self): # 第1个窗体
        def gotomain():
            root1.destroy() # 关闭第1个窗体
            self.loginInterface() # 返回主窗体clear

    
        root1=Tk()
        root1.geometry('700x700')
        root1.title('welcome member login')

        Label(root1, text='用户名:').place(x=100, y=200)
        Label(root1, text='密  码:').place(x=100, y=250)

        # 用户名输入框
        var_usr_name = StringVar()
        entry_usr_name = Entry(root1, textvariable=var_usr_name)
        entry_usr_name.place(x=150, y=200)

        # 密码输入框
        var_usr_pwd = StringVar()
        entry_usr_pwd = Entry(root1, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=150, y=250)


        # 登录 登出
        bt_login = Button(root1, text='登录', width=10, height=1, command=lambda: self.loginInfo(entry_usr_name.get(), entry_usr_pwd.get(), 2, root1))
        bt_login.place(x=100, y=280)

        bt_logquit = Button(root1, text='退出', width=10, height=1, command=lambda:gotomain)
        bt_logquit.place(x=220, y=280)


        but = Button(root1, text="return to main interface",command=gotomain)
        but.pack(pady=10)


        root1.mainloop()

    def registerGuest2Menber(self, root2, user):
        root2.destroy()
        root = Tk()
        root.geometry('900x700')
        root.title('welcome register interface')
        messagebox.showinfo('Guest', 'you should register first.')

        
        # 创建一个member对象, shoppingCart非空
        userOL = []
        userShopping = user.ShoppingCart

        Label(root, text='personName:').place(x=100, y=100)
        Label(root, text='userName:').place(x=100, y=140)
        Label(root, text='password:').place(x=100, y=180)
        Label(root, text='email:').place(x=100, y=220)
        Label(root, text='id:').place(x=100, y=260)
        Label(root, text='streeName:').place(x=100, y=300)
        Label(root, text='city:').place(x=100, y=340)
        Label(root, text='postcode:').place(x=100, y=380)
        Label(root, text='phone:').place(x=100, y=420)


        temp = StringVar()
        personName = Entry(root, textvariable=temp)
        personName.place(x=180, y=100)

        temp1 = StringVar()
        userName = Entry(root, textvariable=temp1)
        userName.place(x=180, y=140)

        temp2 = StringVar()
        password = Entry(root, textvariable=temp2)
        password.place(x=180, y=180)

        temp3 = StringVar()
        email = Entry(root, textvariable=temp3)
        email.place(x=180, y=220)

        temp4 = StringVar()
        id = Entry(root, textvariable=temp4)
        id.place(x=180, y=260)

        temp5 = StringVar()
        streeName = Entry(root, textvariable=temp5)
        streeName.place(x=180, y=300)

        temp6 = StringVar()
        city = Entry(root, textvariable=temp6)
        city.place(x=180, y=340)

        temp7 = StringVar()
        postcode = Entry(root, textvariable=temp7)
        postcode.place(x=180, y=380)

        temp8 = StringVar()
        phone = Entry(root, textvariable=temp8)
        phone.place(x=180, y=420)

        userOL = []
        
        but = Button(root, text='确认', width=10, height=1, command=lambda:self.guestTemp(personName.get(), userName.get(), password.get(), email.get(), id.get(), streeName.get(), city.get(), postcode.get(), phone.get(), userShopping, userOL, root))
        but.place(x=350, y=450)

        root.mainloop()

    def guestTemp(self, personName, userName, password, email, id, streeName, city, postcode, phone, userShopping, userOL, root2):

        memAdd = Address(streeName, city, postcode)
        
        user = Member(personName, userName, password, email, id, memAdd, phone, userShopping, userOL)

        self.memberMenue(user, root2)


    def guestMenue(self, root2, guestUser):
        def gotomain():
            root.destroy() # 关闭第1个窗体
            self.loginInterface() # 返回主窗体clear

        root2.destroy()
        root = Tk()
        root.geometry('900x700')
        root.title('welcome member')

        # products
        label1= Label(root,text="products")
        label1.place(x=100, y=29)
        prod = scrolledtext.ScrolledText(root, width=100, height=10)
        prod.place(x=100, y=50)
        
        # show search result
        label2= Label(root,text= 'show search result')
        label2.place(x=100, y=220)
        searchRes = scrolledtext.ScrolledText(root, width=100, height=10)
        searchRes.place(x=100, y=250)

        # search product
        prodFindEntry = Entry(root)
        prodFindEntry.place(x=200, y=15)
        prodFindBut = Button(root, text='search product by id', width=20, height=1, command=lambda:self.findProduct(prodFindEntry, searchRes))
        prodFindBut.place(x=400, y=10)
        emptyFind = Button(root, text='empty', width=10, height=1, command=lambda:self.emptyProduct(searchRes))
        emptyFind.place(x=600, y=390)
        

        # show all products
        productList = self.products
        for item in productList:
            # print(item)
            pritprodDesc = 'prodDesc: '+item[1]
            pritprodPrice = 'prodPrice: ' + item[2]
            pritCateId = 'cateID: '+item[3]
            pritCateDesc = 'cateDesc: '+item[4]
            
            prod.insert('end', 'prodID: '+item[0] + ' ')
            prod.insert('end', pritprodDesc.ljust(30, ' '))
            prod.insert('end', pritprodPrice.ljust(15, ' '))
            prod.insert('end', pritCateId.ljust(10, ' '))
            prod.insert('end', pritCateDesc.ljust(10, ' '))
            prod.insert('end', '\n')


        # guestUser's shoppingcart:初试状态下购物车为空
        label3= Label(root,text= guestUser.getName() + " shoppingcart")
        label3.place(x=100, y=420)
        shopping = scrolledtext.ScrolledText(root, width=100, height=10)
        shopping.place(x=100, y=450)

        #add & remove & empty
        # Detail button:根据鼠标选中的名字，在文本框显示详情
        button1 = Button(root, text='add', width=10, height=1, command=lambda:self.addProduct(prod, shopping, guestUser))
        button1.place(x=100, y=600)

        button2 = Button(root, text='remove', width=10, height=1, command=lambda:self.removeProduct(shopping, guestUser))
        button2.place(x=200, y=600)

        button3 = Button(root, text='empty', width=10, height=1, command=lambda:self.emptyProduct(shopping))
        button3.place(x=300, y=600)

        button4 = Button(root, text='make order', width=20, height=1, command=lambda:self.registerGuest2Menber(root, guestUser))
        button4.place(x=400, y=600)

        but = Button(root, text="return to main interface",command=gotomain)
        but.place(x=600, y=10)
        
        root.mainloop()


    def guest(self): # 第2个窗体
        def gotomain():
            root2.destroy() # 关闭第2个窗体
            self.loginInterface() # 返回主窗体
            
        root2=Tk()
        root2.geometry('700x700')
        root2.title('welcome guest view')


        # create a guest
        gname = 'guest9527'
        userShopping = ShoppingCart([])
        user = Guest(gname, userShopping)
        # self.guestMenue(root2, user)

        but1=Button(root2,text="welcome to guset channel",command=lambda:self.guestMenue(root2, user))
        but1.place(x=220, y=200)

        but2 = Button(root2, text="return to main interface",command=gotomain)
        but2.place(x=220, y=250)

        root2.mainloop()

    def staff(self): # 第3个窗体
        def gotomain():
            root3.destroy() # 关闭第3个窗体
            self.loginInterface() # 返回主窗体
            
        root3=Tk()
        root3.geometry('700x700')
        root3.title('welcome staff login')

        Label(root3, text='用户名:').place(x=100, y=200)
        Label(root3, text='密  码:').place(x=100, y=250)

        # 用户名输入框
        var_usr_name = StringVar()
        entry_usr_name = Entry(root3, textvariable=var_usr_name)
        entry_usr_name.place(x=150, y=200)

        # 密码输入框
        var_usr_pwd = StringVar()
        entry_usr_pwd = Entry(root3, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=150, y=250)

        # 登录 登出
        
        bt_login = Button(root3, text='登录', width=10, height=1, command=lambda: self.loginInfo(entry_usr_name.get(), entry_usr_pwd.get(), 1, root3))
        bt_login.place(x=100, y=280)


        bt_logquit = Button(root3, text='退出', width=10, height=1, command=lambda: self.logoutInfo(entry_usr_name.get(), 1))
        bt_logquit.place(x=220, y=280)
        

        but = Button(root3, text="return to main interface",command=gotomain)
        but.pack(pady=10)

        root3.mainloop()



if __name__ == '__main__':
    
    onlineshop = OnlineShopping()

    myGUI(onlineshop).loginInterface()
