# -*- coding: utf-8 -*-

a= int(input("1.sayıyı giriniz:"))
fak=1
if a<0:
    print("Negatif sayıların Faktöriyeli Olmaz")
    
elif a==0:
    print("sonuc:1")
else:
    for i in range(1,a+1):
        fak=fak*i
    print("sonuc",fak)    