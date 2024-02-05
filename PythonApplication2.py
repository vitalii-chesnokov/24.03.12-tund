nimed=["Mati","Kati","Mati","Mati", "kadri" ]
while True:
    valik=input("Andmete lisamine-add\nAndmete näitamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sorrtimine-sort\nAndmete otsing-ots\n")
    if valik=="add":
        valik=input("Kas lisame mitu inimest(mitu) või positsioonile(pos)")
        if valik=="mitu":
            mitu=int(input("Mitu inimest lisame?"))
            for i in range(mitu):
                nimi=input("Sisesta nimi: ")
                nimed.append(nimi)
        else:
            indeks=int(input("Kuhu lisamine? "))
            nimi=input("Mis nimi: ")
            nimed.insert(indeks-1,nimi)
    elif valik=="del":
        valik=input("Kas kustutamine nimi või indeksu järgi (ind)?")
        if valik=="nimi":1
            nimi=input("Mis nimi on vaja kustutada? ")
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber"))
            nimed.pop(indeks-1)
    elif valik=="show":
        print(nimed)
    elif valik=="rev":
         nimed.reverse()
         print(nimed)
    elif valik=="sort":
        nimed.sort()
    elif valik=="clear":
        print(nimed.clear())
    elif valik=="ots":
        ind=-1
        nimi=input("MIs nimi otsimine ?")
        if nimed.count(nimi)>0:
            for i in range(len(nimed)):
              ind=nimed.index(nimi,ind+i)
              print(f"  {nimi} on indeksiga {ind} ")
    else:
        print(f"{nimi}ei elo nimekirjas")