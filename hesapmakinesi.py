# -*- coding: utf-8 -*-

def topla(sayi1,sayi2):
    return sayi1+sayi2

def cıkar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2

print("Operasyon:")
print("1: Toplama")
print("2:Çıkarma")
print("3:Çarpma")
print("4:Bölme")

secenek=input("Operasyon Seciniz:")

sayi1=int(input("1. Sayıyı Giriniz:"))
sayi2=int(input("2. Sayıyı Giriniz:"))

if secenek=='1':
    print("Toplam:"+str(topla(sayi1,sayi2)))
    
    
    
elif secenek=='2':
    print("Çıkarma:"+str(cıkar(sayi1,sayi2)))


elif secenek=='3':
    print("Çarpma:"+str(carp(sayi1,sayi2)))

elif secenek=='4':
    print("Bölme:"+str(bol(sayi1,sayi2)))

else:
    print("Lütfen Geçerli Bir Seçim Yapınız:")
    









    
    

