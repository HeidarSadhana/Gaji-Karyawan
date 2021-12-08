def gaji_karyawan(level,maks_bungkus,coklat,strawberry,kacang):
    if level == "A":
        gaji = 7000
        bonus = level_a(maks_bungkus,coklat,strawberry,kacang)    
        gaji += gaji*bonus
        print('Bonus Gaji :',round(bonus*100),"%")
        return gaji
    if level == "B":
        gaji = 5000
        bonus = level_b(maks_bungkus,coklat,strawberry,kacang)    
        gaji += gaji*bonus
        print('Bonus Gaji :',round(bonus*100),"%")
        return gaji
    if level == "C":
        gaji = 3000
        bonus = level_c(maks_bungkus,coklat,strawberry,kacang)    
        gaji += gaji*bonus
        print('Bonus Gaji :',round(bonus*100),"%")
        return gaji
        
def level_a(maks_bungkus,coklat,strawberry,kacang):
    bonus = 0
    coklat,kacang,strawberry = int(coklat),int(kacang),int(strawberry)

    if 5001 <= coklat <= 6000:
        maks_bungkus -= coklat
        bonus += 35/100
    elif 4000 <= coklat <= 5000:
        maks_bungkus -= coklat
        bonus += 30/100
    elif 3000 <= coklat <= 3999:
        maks_bungkus -= coklat
        bonus += 25/100
    
    if 5001 <= strawberry <= 6000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 40/100
    elif 4000 <= strawberry <= 5000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 30/100 
    elif 3000 <= strawberry <= 3999:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 15/100

    if 5001 <= kacang <= 6000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 40/100
    elif 4000 <= kacang <= 5000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 30/100 
    elif 3000 <= kacang <= 3999:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 15/100

    return bonus

def level_b(maks_bungkus,coklat,strawberry,kacang):
    bonus = 0
    coklat,kacang,strawberry = int(coklat),int(kacang),int(strawberry)
    
    if 5001 <= coklat <= 6000:
        maks_bungkus -= coklat
        bonus += 25/100
    elif 4000 <= coklat <= 5000:
        maks_bungkus -= coklat
        bonus += 20/100 
    elif 3000 <= coklat <= 3999:
        maks_bungkus -= coklat
        bonus += 15/100

    if 5001 <= strawberry <= 6000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 30/100
    elif 4000 <= strawberry <= 5000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 20/100 
    elif 3000 <= strawberry <= 3999:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 7/100

    if 5001 <= kacang <= 6000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 30/100
    elif 4000 <= kacang <= 5000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 20/100 
    elif 3000 <= kacang <= 3999:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 7/100

    return bonus

def level_c(maks_bungkus,coklat,strawberry,kacang):
    bonus = 0
    coklat,kacang,strawberry = int(coklat),int(kacang),int(strawberry)
    
    if 5001 <= coklat <= 6000:
        maks_bungkus -= coklat
        bonus += 25/100
    elif 4000 <= coklat <= 5000:
        maks_bungkus -= coklat
        bonus += 20/100 
    elif 3000 <= coklat <= 3999:
        maks_bungkus -= coklat
        bonus += 15/100

    if 5001 <= strawberry <= 6000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 30/100
    elif 4000 <= strawberry <= 5000:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 20/100 
    elif 3000 <= strawberry <= 3999:
        maks_bungkus -= strawberry
        if maks_bungkus >= 0:
            bonus += 7/100

    if 5001 <= kacang <= 6000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 30/100
    elif 4000 <= kacang <= 5000:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 20/100 
    elif 3000 <= kacang <= 3999:
        maks_bungkus -= kacang
        if maks_bungkus >= 0:
            bonus += 7/100

    return bonus

def bungkus(jenis):
    bungkus =  input('Jumlah Bungkus {} (1 bulan) : '.format(jenis))
    bungkus_angka = bungkus.isdigit()
    while bungkus_angka == False:
        bungkus = input('Jumlah Bungkus (1 bulan) : ')
        bungkus_angka = bungkus.isdigit()
    return bungkus

nama = input('Nama Karyawan : ')
level = input('Level Karyawan : ')
while level not in ['A','B','C']:
    level = input('Level Karyawan : ')

coklat = bungkus('Coklat')
strawberry = bungkus('Strawberry')
kacang = bungkus('Kacang')

maks_bungkus = 6000
gaji = gaji_karyawan(level,maks_bungkus,coklat,kacang,strawberry)

print("Gaji :",gaji)