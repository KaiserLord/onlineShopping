class Product():
    """ The Product Class"""

    def __init__(self, productID:int, productDescription:str, 
                price:float, categoryID, categoryDesc, qty=1):
        """! The Initialiser
        @param ProductID product id
        @param productDescription product description
        @param price product price
        @param productCategory product category
        """

        self.productID = productID
        self.productDescription = productDescription
        self.price = price
        self.categoryID = categoryID
        self.categoryDesc = categoryDesc
        self.qty = qty

    def getProductDetails(self):
        """! get product information"""

        return self.productDetails
        
    def __str__(self) -> str:

        res = 'productID:{}\tproductDescription:{}\tprice:{}\tcategoryID:{}\tcategoryDesc:{}\n'.format(self.productID, self.productDescription, self.price, self.categoryID, self.categoryDesc)
        return res