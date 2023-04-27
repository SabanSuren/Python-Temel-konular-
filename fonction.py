# -*- coding: utf-8 -*-


def selamver(isim ="ziyaretci"):
    print("merhaba" +  isim)
    
selamver("Şaban")    
selamver("asiye")
selamver("kerem")
selamver("yasir")
selamver("azra")

def selamver2(isim, soyisim="süren"):
    print("merhaba" + isim + " "  + soyisim)
    
selamver2("Şaban")
selamver2("Şaban","süren")    
#%%
a= int(input("1.sayıyı giriniz:"))
b=int(input("2.sayıyı giriniz:"))
def alan(a,b):
    return a*b/2

sonuc=alan(a,b)
print(sonuc)
#%%
alan2= lambda a,b : a*b/2

print(alan2(5,6))

print(type(alan2))
x=alan2
print(x(4,7))