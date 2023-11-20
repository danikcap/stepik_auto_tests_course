class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        res = 1
        while self.s and self.s[-1][0] <= price:
            res += self.s[-1][1]
            self.s.pop()
        self.s.append([price, res])
        return res


my = StockSpanner()
# print(my.next(100))
# print(my.next(80))
# print(my.next(60))
# print(my.next(70))
# print(my.next(60))
# print(my.next(75))
# print(my.next(85))

# [1, 1, 1, 2, 1, 4, 6]

print(my.next(28))
print(my.next(14))
print(my.next(28))
print(my.next(35))