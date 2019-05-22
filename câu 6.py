class str1():
    def __init__(self, str1):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.str1.upper())


str1.get_String()
str1.print_String()