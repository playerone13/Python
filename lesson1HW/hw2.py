time = int(input("введите время в секундах - "))
m = time // 60
m1 = time % 60
h = m // 60
s = time % 60
print(f"{h:02}:{m1:02}:{s:02}")