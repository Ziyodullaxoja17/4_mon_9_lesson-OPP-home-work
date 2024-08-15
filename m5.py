from os import system 
system("cls")

class Numbers:
    def __init__(self, first=None, second=None, third=None, fourth=None, fifth=None):
        self.numbers = [first, second, third, fourth, fifth]

    def delete_last_item(self):
        
        self.numbers = [num for num in self.numbers if num is not None]
        if self.numbers:
            self.numbers.pop()
        return self

    def info_numbers(self):
        return ', '.join([str(num) for num in self.numbers if num is not None])

numbers = Numbers(23, 45, 32, 65, 26)


new_numbers = numbers.delete_last_item()
new1_numbers = new_numbers.delete_last_item()
new2_numbers=new1_numbers.delete_last_item()

print(new2_numbers.info_numbers())

