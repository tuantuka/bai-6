class Hinhchunhat(object):
    def __init__(self, d, r):
        self.dai = d
        self.rong = r

    def area(self):
        return self.dai * self.rong

d = int(input("Chiều dài = "))
r = int(input("Chiều rộng = "))
DientichHCN = Hinhchunhat(d, r)
print("Diện tích hình chữ nhật = ", DientichHCN.area())