from os import system 
system("cls")

class Bino :
     def __init__(self,balanklik,rangi) :
          self.balanklik=balanklik
          self.rangi=rangi

     def get_balandlik(self):
          return self.balanklik
     def get_info(self):
          return f"balandligi : {self.balanklik}   rangi  : {self.rangi}"

     

bino1=Bino(78,"red")
bino2=Bino(45,"green")
bino3=Bino(90,"black")
bino4=Bino(56,"yellow")
bino5=Bino(34,"white")

binolar=[bino1,bino2,bino3,bino4,bino5]


filter_bino=list(filter(lambda bino : bino.balanklik>50,binolar))


for bino in filter_bino:
     data=bino.get_info()
     print(data)
     






          
