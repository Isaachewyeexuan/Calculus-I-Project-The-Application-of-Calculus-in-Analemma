import math

B = float(input("B_0= "))
N = int(input("n= "))

for i in range(1,N+1,1):
    B = B - (19.74*math.cos(2*B) + 7.53*math.sin(B) - 1.5*math.cos(B))/(-39.48*math.sin(2*B) + 7.53*math.cos(B) + 1.5*math.cos(B))
    print(f"B_{i} = {B}")

print("----------")

t = (365/(2*math.pi))*B +81
print(f"t = {t}")

print("----------")

E = 9.87*math.sin(2*B) - 7.53*math.cos(B) - 1.5*math.sin(B)
print(f"E = {E}")