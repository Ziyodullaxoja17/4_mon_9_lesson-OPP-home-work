from os import system
system("cls")


class Car :
     def __init__(self,brand):
          self.brand=brand
     def get_brand_name (self):
          return self.brand
          

car1=Car("Ferari")
car2=Car("Bugatti")
car3=Car("BMV")
car4=Car("Chevrolet")

cars=[car1,car2,car3,car4]

mashinalar_brand=[]
for mashina in cars :
     result=mashina.get_brand_name()
     mashinalar_brand.append(result)

print(mashinalar_brand)
print("\n")

mashina_name=input("mashina nomini kiriting  =>  ")

natija =True
if mashina_name in mashinalar_brand:
     natija = True
else:
     natija= False


print(natija)
