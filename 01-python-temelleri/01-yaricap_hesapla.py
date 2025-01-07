# yarıçapı verilen dairenin alan ve çevresini hesaplayınız
 
# daire alanı   : πr²
# daire çevresi : 2πr

pi = 3.14

r = float(input("yarıçapı giriniz : "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan : ", alan)
print("çevre : ", cevre)