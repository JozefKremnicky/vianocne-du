subor=open('skok_do_dialky.txt','r')
povod={}
maximalnadlzka = 0
vitaz = []
for riadok in subor:
    udaje=riadok.split()
    povod[udaje[1]]=povod.get(udaje[1],0)+1
    dlzka=0
    for i in range(5):
        dlzka = max (dlzka, int(udaje[i+2]))
    if dlzka > maximalnadlzka:
        maximalnadlzka = dlzka
        vitaz=[udaje[0]]
    elif dlzka == maximalnadlzka:
        vitaz.append(udaje[0])
print ('Zoznam krajin pôvodu:')
print ('Najdlhsi skok:', maximalnadlzka)
for vitaz in vitaz:
    print (vitaz)
