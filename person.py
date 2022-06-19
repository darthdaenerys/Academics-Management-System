from address import Address

class Person:
    def __init__(self,first,last,dob,phone,addresses):
        self.first=first
        self.last=last
        self.dob=dob
        self.phone=phone
        self.addresses=[]
        if isinstance(addresses,Address):
            self.addresses.append(addresses)
        elif isinstance(addresses,list):
            for i in addresses:
                if not(isinstance(i,Address)):
                    raise Error("Invalid address object")
                else:
                    self.addresses.append(i)
        else:
            raise Error('Invalid object passed')

    def add_address(self,address):
        if not(isinstance(address,Address)):
            raise Error('Invalid address')
        self.addresses.append(address)