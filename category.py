from product import Product

class Category():
    """! The Category Class"""

    def __init__(self,categoryID:str, categoryDesc:str, productList):
        """! The initialiser
        @param categoryID category id
        @param categoryDesc category description
        @param productList list of product
        """
        self.categoryID = categoryID
        self.categoryDesc = categoryDesc
        self.productList = productList
    
    def countProduct():
        """! get the amount of products in the category"""
        pass

    def getProductList():
        """! get a list of products"""
        pass

if __name__ == '__main__':
    p1 = Product(101, 'Retro Skateboard', 20.00, 1)
    p2 = Product(102, 'Swim Seat', 15.00, 1)
    productList = []
    productList.append(p1) #传入到购物车的是list
    productList.append(p2)

    c = Category('c001', '雅思噶', productList)