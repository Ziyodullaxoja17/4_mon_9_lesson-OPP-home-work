from os import system 
system("cls")


class Talaba:
     def __init__(self,ism,familiya,ball):
          self.ism=ism
          self.familiya=familiya
          self.ball=ball
     def get_ball(self):
          return self.ball
     def get_name(self):
          return self.ism
     


talaba1=Talaba("Ziyodulla","Tursunboyev",90)
talaba2=Talaba("Nodir","Axmatov",83)
talaba3=Talaba("Mashxura","Nematova",78)


talabalar=[talaba1,talaba2,talaba3]

talabalar_balli=[]


for student in talabalar:
    ball_student=student.get_ball()
    talabalar_balli.append(ball_student)

print(talabalar_balli)

min=min(talabalar_balli)


for talaba in talabalar:
     if talaba.get_ball() == min:
          name_min=talaba.get_name()



print(f"talaba ismi : {name_min} \nballi       : {min}")



