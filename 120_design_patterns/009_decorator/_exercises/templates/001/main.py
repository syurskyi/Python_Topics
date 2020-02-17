import coffeeshop

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))