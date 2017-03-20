class ShoppingCart():
	def  __init__(self):
		self.total = 0
		self.items ={}
	def add_item(self,item_name,quantity,price):
		if  not item_name in self.items:
			self.items[item_name] = quantity
			self.total += (price * quantity)
		else:
			self.total += (price * quantity)
		
	def remove_item(self,item_name,quantity,price):
		if item_name in self.items:
			if quantity > item_name[quantity]:
				del self.items[item_name]
				self.total -= (price * quantity)
				return self.items
			else:
				del self.items[item_name]
				self.total -= (price * quantity)
				return self.items


	def checkout(self,cash_paid):
		if cash_paid < self.total:
			return 'Cash paid not enough'
		elif cash_paid == self.total:
			return 'Cost fully paid'

		else:
			balance = self.total - cash_paid
			return balance

class Shop(ShoppingCart):
	def __init__(self):
		self.quantity = 100

	def remove_item(self):
		self.quantity -= 1





class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if not item_name in self.items:
           self.total += (quantity * price)
           self.items[item_name] = quantity
        
    def remove_item(self, item_name, quantity, price):
        if quantity > self.items[item_name]:
            self.items[item_name] = 0
            self.total-= (quantity * price)
        else:
            self.items[item_name]-= quantity
            self.total-=  (quantity * price) 
        
    def checkout(self, cash_paid):
        if self.total > cash_paid:
            return 'Cash paid not enough'
        else:
            return (cash_paid - self.total)
            
class Shop(ShoppingCart):
  
    def __init__(self):
        self.quantity = 100
    
    def remove_item(self):
		self.quantity -= 1