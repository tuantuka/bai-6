import math
class Circle(object):
    def __init__(self, R):
        self.bankinh = R

    def chuvi(self):
        return float(self.bankinh * 2 * math.pi)

    def dientich(self):
        return float(self.bankinh * self.bankinh * 2 * math.pi)

R = float(input("Bán kính hình tròn = "))
ChuviHT = Circle(R)
DientichHT = Circle(R)
if R <= 0:
    print("Bán kính không hợp lệ")
else:
    print("Chu vi hình tròn = ", ChuviHT.chuvi())
    print("Diện tích hình tròn = ", DientichHT.dientich())