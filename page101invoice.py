
class Invoice:
  def __init__(self,partnumber,partdescription,quantity,price_per_item ):
     self.partnumber=partnumber
     self.partdescription=partdescription
     self.quantity=quantity
     self.price_per_item=price_per_item
  
   
   
  def getInvoiceAmount(self):
           return self.quantity*self.price_per_item
    

print("----------------------------------")

h=Invoice("2", "green hammer",34,1)

print ("Your payable amount is",h.getInvoiceAmount())
