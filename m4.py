from os import system 
system("cls")

class items:
    def __init__(self, first=None, second=None, third=None, fourth=None, fifth=None):
        self.items = [first, second, third, fourth, fifth]

    def delete_last_item(self):
        
        self.items = [num for num in self.items if num is not None]
        if self.items:
            self.items.pop()
        return self

    def my_list_print(self):
        return ', '.join([str(num) for num in self.items if num is not None])
    



items = items('j', 34.234, True, 65, "Hello")


new_items = items.delete_last_item()
new1_items = new_items.delete_last_item()
new2_items=new1_items.delete_last_item()

print(new2_items.my_list_print())

