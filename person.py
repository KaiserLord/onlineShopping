class Person():
    """! The Person Class
    The parent class
    """
    def __init__(self,personName):
        """! The initialiser for Person
        @param personName person's names
        """
        self.personName = personName
        print('This Person class')


    def getName(self):
        """! get person's names"""
        return self.personName

if __name__ == '__main__':
    p = Person('理查德')