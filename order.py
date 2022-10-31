from datetime import datetime
from address import Address
from payment import Payment
from orderline import OrderLine
from product import Product

class Order():
    """! The Order Class"""

    def __init__(self, orderID:int, orderStatus:int, orderDate:datetime, 
                orderTotal:float, shippingCost:float, shippingAddress:Address,
                paymentDetails:Payment, orderDet:list[OrderLine]):
        """! The initialiser
        @param orderID order id
        @param orderStatus order status
        @param orderDate order date
        @param orderTotal total cost for order
        @param shippingCost shipping cost
        @param shippingAddress shipping address
        @param paymentDetails payment details
        @param orderDet orderLine list
        """
        self.orderID = orderID
        self.orderStatus = orderStatus
        self.orderDate = orderDate
        self.orderTotal = orderTotal
        self.shippingCost = shippingCost
        self.shippingAddress = shippingAddress
        self.paymentDetails = paymentDetails
        self.orderDet = orderDet

    def updateStatus(self, status:int):
        """! update order status"""
        self.orderStatus = status


    def updatePayment(self, pay:Payment):
        """! update payment information"""
        pay.paymentAmt = 0.0

    def updateShippingAdd(self, address:Address):
        """! update shipping address"""
        self.shippingAddress = address
    
    def __str__(self) -> str:
        # 显示传入订单的status,把数字转换成对应的str文字
        status = ''
        if self.orderStatus == 0:
            status = 'processing'
        elif self.orderStatus == 1:
            status = 'awaiting shipment'
        elif self.orderStatus == 2:
            status = 'shipped'
        elif self.orderStatus == 3:
            status = 'delivered'
        else:
            status = 'closed'
        res = '----------\norderID:{}\torderStatus:{}\torderDate:{}\torderTotal:{}\tshippingCost:{}'.format(self.orderID, status, self.orderDate, self.orderTotal, self.shippingCost)

        
        # + self.orderID + status + self.orderDate + ' ' + str(self.orderTotal) + str(self.shippingCost) 
        # res += self.shippingAddress.getAddress() + self.paymentDetails.paymentAmt
        return res


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


    time_now = datetime.now()
    o = Order(121, 1, time_now, 20.5, 50, ad, py, olList)
    print(o.shippingAddress.getAddress())
    
