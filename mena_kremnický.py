subor = open ('mena_zamestnancov.txt')
mena = subor.readlines()
for i in range(len(mena)):
    mena[i]= mena [i].strip()
    pocet= len (mena)//2
    print('Pocet mien:',pocet)
    krstne=mena[:pocet]
    priezviska = mena[:pocet]
    dlzka = 0
    for s in priezviska:
        dlzka=max (dlzka, len(s))
print('Najdlhsie priezvysko',dlzka)
dlzka = 0
for s in krstne:
    dlzka= max(dlzka,len(s))
print('Najdlhsie krsne meno',dlzka)
vystup = open ('vypis.txt','w')
for i in range (pocet):
    vystup.write(krstne[i])+(''*(dlzka-len(krstne[i])+1))
vstup.close()
