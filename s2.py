# SQL ODEV

# 3. Customers tablosunda hangi ülkeden kaçar tane müşteri olduğunu bulunuz.















#************ GOSTERIM SEKILLERI **************

x1 = {'antricoat': 25.3, 'beef': 33.8, 'chicken': 22.7}

x2 = dict([('antricoat', 25.3), ('beef', 33.8), ('chicken', 22.7)])

x3 = dict(antricoat=25.3, beef=33.8, chicken=22.7)


#*********** EKLEME VEYA DEGISIKLIK *************
x1['beef'] = 25.2

#*********** ELEMAN SILMEK ICIN *****************
del x1['beef']

#*********** ELEMAN SAYISI **********************
len(x1)

#*********** TUM ELEMANLERI SILMEK ICIN *********
x1.clear()

#*********** SOZLUK SILMEK ICIN *********
del x1

#************ ELEMAN KONTROLU SAGLAMA ***********
print('chicken' in x2)

#*********** ANAHTARLARA ULASMAK ICIN ************
print("keys of x3: ", x3.keys())

#*********** DEGERLERE ULASMAK ICIN **************
print("values of x3: ", x3.values())

#*********** ANAHTAR VE DEGERLERE ULASMAK ICIN ****
print("items of x3: ", *[i for i in x3.items()])

#************ DEGERLER KONTROLU SAGLAMA ***********
print(10 in x2.values())

#************ ITERASYONLA KEYS BULMA ********
for key in x3:
    print(key)    # veya print(key, x3[key])


#************ ITERASYONLA KEY-VALUE BULMA ********
for key, value in x3.items():
    print(key, value)

#************ DICT OZELLIKLERI *******************

print(dir(x3))

help(x3.pop)                               # mesela pop ozelliginin ne ise yaradigini ogrenmek icin
lamp = x3.pop("lamp meat", None)           # burada None yazmazsak KeyError verir
print(lamp)                                # gormek icin
