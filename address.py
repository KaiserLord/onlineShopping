
class Address:
    def __init__(self, streeName, city, postcode):
        self.streeName = streeName
        self.city = city
        self.postcode = postcode
    
    def getAddress(self):
        return self.streeName + ' ' + self.city +  ' ' + str(self.postcode)
    
    def __str__(self) -> str:
        return '\nAddress:{}\tcity:{}\tpostcode:{}'.format(self.streeName, self.city, self.postcode)