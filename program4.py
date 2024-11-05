#1st program
#print((9**0.5)*5)
#2nd program
#print(9.99>9.98 and 1000 !=1000.1)
##3d program
#print(2*2+2)
#print(2*(2+2) ==2*2+2)
#4th program
str_1= '123.456'
str_2=float(str_1)*10 # получаем str_2 = 1234.56
ost_1 = str_2 % 1 # вычисляем остаток (после запятой) от str_2 и получаем 0.56
str_3=(str_2-ost_1)# отрезаем остаток от str_2 и получаем 1234.0
str_4=str_3 % 10 # отрезаем 4 и запоминаем в str_4
print(int(str_4))