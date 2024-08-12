import random
import string

rakamlar=string.digits
semboller=string.punctuation
kucuk_harfler=string.ascii_lowercase
buyuk_harfler=string.ascii_uppercase
tum_karakterler=[rakamlar,semboller,kucuk_harfler,buyuk_harfler]

sifre=""

for j in range(4):
    for i in range(2):
        sifre+= tum_karakterler[j][random.randint(0,9)]

sifre=list(sifre)
random.shuffle(sifre)


yeni_sifre=""
yeni_sifre=yeni_sifre.join(sifre)

print(yeni_sifre)