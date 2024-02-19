1. laboratorijska vježba  (0036526060)

Analiza i projektiranje računalom

Korištena verzija Python-a i razvojno okruženje:
Za izradu vježbe korištena je verzija Pythona python3.10 te je korišteno razvojno okruženje PyCharm 2022.1.2.

Upute za pokretanje zadataka za vježbu:

U datoteci Main izrađene su sve potrebne matrice za rješavanje svih zadataka te pokretanjem spomenutog programa u IDE-u poput PyCharm-a svi se zadaci izvršavaju te se rezultat
ispisuje na ekran. Kod korištenja IDE-a, ulazne datoteke bi trebale biti smještene u direktoriju projekta.
U slučaju korištenja naredbenog retka (Command Propmt-a), pozicioniranjem u src folder (folder sa Main.py i Matrica.py datotekom) te pokretanjem naredbe py Main.py, rezultati će se ispisati 
na ekran. U tom slučaju datoteke sa zapisima podataka o matricama moraju biti smješteni u spomenuti src folder u kojemu ste pozicionirani.


Opis sustava i upute za korištenje:
Datoteka Matrica.py sadržava klasu Matrica koja omogućava jednostavno rukovanje objektima tipa dvodimenzionalne matrice.
Objekt tipa Matrica kreira se tako da se pruža putanja do datoteke gdje su zapisani podaci o matrici, a mogu se dati i samo dimenzije matrice
čime se kreira matrica odgovarajućih dimenzija napunjena nulama. Moguće je i ne pružiti nikakve podatke o Matrici te se time samo kreira objekt tipa Matrica, no ne i elementi matrice.

Primjer: A = Matrica("A.txt")
         B = Matrica(x=1,y=1)
         C = Matrica()

Naredba kojom se jedna matrica pridružuje drugoj, A=B, ostvarena je metodom assign te funkcionira na način da matrica dobiva elemente njoj
pridružene matrice, no ne postaje referenca na taj objekt.

Primjer: A.assign(C)

Čitanje podataka o matrici te spremanje u dvodimenzionalno polje ostvareno je u metodi createMatrix(). Iz datoteke se čita red po red te broj
redova odgovara x dimenziji matrice, a onda broj elemenata u svakom retku odvojen space-om odgovara y dimenziji, tj. broju stupaca. U istoj se metodi matrica
inicijalizira tako da se puni nulama u slučaju da nije pružena putanja do datoteke s podacima o matrici, već samo njene dimenzije.

Metoda printMatrix služi za ispisivanje matrice na ekran, a to je ostvareno time što je overload-ana metoda koja predstavlja string reprezentaciju
instance klase Matrica. Metoda storeElements služi za ispisivanje matrice u novostvorenu datoteku u formatu iz kojega se i čita.

Primjer: A.printMatrix()
         A.storeElements()



Metode za postavljanje i dohvat elementa matrice ostvarene su overloading-om metoda __setitem__ i __getitem__.
Primjer korištenja:

        A[0,0] = x          #Ovdje se zove nadjačani __setitem__, x je vrijednost tipa float koji se sprema na željenu poziciju
        x = A[1,1]          #Ovdje se zove nadjačani __getitem__, x je vrijednost tipa float u koju se sprema dohvaćeni element

Metode za zbrajanje, oduzimanje i množenje matrica redom su ostvarene sljedećim nadjačanim metodama:
__add__, __sub__, __mul__, a transponiranje metodom transpose te __rmul__ kada je matrica na desnoj strani operacije množenja.

Primjer:  A+C
          A-C
          A-2
          A+2
          A*C
          A*2
          A.transpose()
          3*B #zove se __rmul__

Metode koje obavljaju operatore +=, -= i *= ostvarene su nadjačavanjem metoda __iadd__, __isub__ i __imul__.

Primjer: A += B
         A += 2
         A -= B
         A -= 2
         A *= 2
         A *= B

Operator za usporedbu matrica poziva nadjačanu metodu __eq__ u kojoj je implementirana usporedba elemenata dviju matrica.

Primjer: A==B


Supstitucija unaprijed ostvarena je metodom forwardSubstitution, a supstitucija unatrag metodom backwardSubstitution.

Primjer: A.forwardSubstitution()
         B.backwardSubstitution

LU i LUP dekompozicija ostvarena je metodom decomposition koja prima argument koji govori o odluci za metodu dekompozicije (False za LU i True za LUP).
Ona vraća permutacijsku matricu, sumu koja sadrži broj promjena redaka u permutacijskoj matrici, donju trokutastu i gornju trokutastu matricu.

Primjer: P, suma,L, U = A.decomposition(p = True)      #LUP dekompozicija
         P, suma, L, U = B.decomposition(p = False)     #LU dekompozicija

Inverzija je ostvarena nadjačavanjem operatora ~ te vraća inverz matrice ako ga ona sadrži.

Primjer: ~A

Determinanta matrice računa se metodom determinant te vraća determinantu ako nije došlo do pogreške prilikom računanja.

Primjer: A.determinant()