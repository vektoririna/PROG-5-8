class Client():
    def __init__(self, firstname, lastname, email, city, index, address):
        
        #self.__client = {
        #    "firstname": firstname, 
        #    "lastname":lastname, 
        #    "email": email,
        #    "city": city,
        #    "index": index,
        #    "adress": address
        #    }

        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__city = city
        self.__index = index
        self.__address = address


    def __str__(self):
        return f'{str(self.firstname) + " " + str(self.lastname)}'


    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def email(self):
        return self.__email

    @property
    def city(self):
        return self.__city

    @property
    def index(self):
        return self.__index

    @property
    def address(self):
        return self.__address
    
