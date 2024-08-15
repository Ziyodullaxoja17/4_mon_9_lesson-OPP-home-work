from os import system
system('cls')

class Word:
    def __init__(self, word):
        self.word = word

    def _update_string(self):
        
        
          
      
        self.word=self.word[0].upper()+self.word[1:-1].lower() +self.word[-1].upper()



        return self.word
          

gap = input("String tipidagi ma'lumot kiriting: ")

word = Word(gap)
natija = word._update_string()

print(natija)
