class Notebook:
    def __init__(self, firma, model, CPU, DDR, price):
        self.firma = firma
        self.model = model
        self.CPU = CPU
        self.DDR = DDR
        self.price = price

    def info_notebook(self):
        return f"""
Firma  : {self.firma}
Model  : {self.model}
CPU    : {self.CPU}
DDR    : {self.DDR}
Price  : {self.price}
"""


notebook1 = Notebook("Dell", "Inspiron 15", "Intel Core i5", "8GB", "$700")
notebook2 = Notebook("HP", "Pavilion 14", "Intel Core i7", "16GB", "$900")
notebook3 = Notebook("Lenovo", "ThinkPad X1", "Intel Core i7", "16GB", "$1200")
notebook4 = Notebook("Asus", "ZenBook 13", "Intel Core i5", "8GB", "$850")
notebook5 = Notebook("Apple", "MacBook Air", "M1", "8GB", "$1000")


Notebooks=[notebook1,notebook2,notebook3,notebook4,notebook5]

for notebook in Notebooks:
    data=notebook.info_notebook()
    print(data)