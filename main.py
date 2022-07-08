t = input("введите время в секундах")
t = int(t)
m = t // 60
m1 = t % 60
h = m // 60
s = t % 60
print(h, m1, s)