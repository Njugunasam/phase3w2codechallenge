class Customer:
    customers = []

    #Initializes a new Customer instance
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.customers.append(self)

    