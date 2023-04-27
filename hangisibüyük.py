# -*- coding: utf-8 -*-

sayi1= int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
sayi3=int(input("3.sayıyı giriniz:"))

if (sayi1>=sayi2) and(sayi1>=sayi3):
   enbuyuk=sayi1
    
elif (sayi2>=sayi1) and(sayi2>=sayi3):
     enbuyuk=sayi2
    
else :
     enbuyuk=sayi3
     
print("en büyük sayı:",enbuyuk)