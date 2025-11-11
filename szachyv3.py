# szachownica 8x8 (każda komórka = 0)
szachownica = [[0 for _ in range(8)] for _ in range(8)]

# początkowe pozycje figur
szachownica[7][0] = 1   # wieża 1 (oznaczona jako 1)
szachownica[7][3] = 2   # hetman (oznaczony jako 2)
szachownica[7][7] = 3   # wieża 2 (oznaczona jako 3)

# Funkcja rysująca szachownicę
def rysuj(szachownica):
    for i in range(8):
        for j in range(8):
            print(f"[{szachownica[i][j]}]", end=" ")
        print()  # nowa linia po każdym wierszu

# Funkcja zmiany pozycji wieży 1 
def zmiana_w1(x, y):
    # Usuwamy poprzednią wieżę 1
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 1:
                szachownica[i][j] = 0
    # Wstawiamy na nową pozycję, jeśli wolna
    if szachownica[x][y] == 0:
        szachownica[x][y] = 1
    else:
        print('Inna figura już znajduje się na tej pozycji!')

# Funkcja zmiany pozycji wieży 2
def zmiana_w2(x, y):
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 3:
                szachownica[i][j] = 0
    if szachownica[x][y] == 0:
        szachownica[x][y] = 3
    else:
        print('Inna figura już znajduje się na tej pozycji!')

# Funkcja zmiany pozycji hetmana 
def zmiana_h(x, y):
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 2:
                szachownica[i][j] = 0
    if szachownica[x][y] == 0:
        szachownica[x][y] = 2
    else:
        print('Inna figura już znajduje się na tej pozycji!')

# Funkcja sprawdzająca, czy dana pozycja jest "szachowana"
def szach(x, y):
    szach_flag = False
    # --- Sprawdzenie poziomów i kolumn (ruch wieży lub hetmana)
    for i in range(8):
        # Sprawdzamy w tym samym wierszu
        if szachownica[x][i] in [1, 2, 3] and i != y:
            print("szach")
            szach_flag = True
        # Sprawdzamy w tej samej kolumnie
        if szachownica[i][y] in [1, 2, 3] and i != x:
            print("szach")
            szach_flag = True

    # --- Sprawdzenie ukośnych (tylko hetman)
    for i in range(1, 8):
        # prawy-dół
        if x+i < 8 and y+i < 8 and szachownica[x+i][y+i] == 2:
            print("szach")
            szach_flag = True
        # lewy-góra
        if x-i >= 0 and y-i >= 0 and szachownica[x-i][y-i] == 2:
            print("szach")
            szach_flag = True
        # prawy-góra
        if x-i >= 0 and y+i < 8 and szachownica[x-i][y+i] == 2:
            print("szach")
            szach_flag = True
        # lewy-dół
        if x+i < 8 and y-i >= 0 and szachownica[x+i][y-i] == 2:
            print("szach")
            szach_flag = True

    if not szach_flag:
        print("Brak szachu")


# Główna pętla programu (menu)
while True:
    print("===== SZACH CZY NIE? =====")
    print("0 - Pokaż szachownicę")
    print("1 - Zmień pozycję wieży 1")
    print("2 - Zmień pozycję wieży 2")
    print("3 - Zmień pozycję hetmana")
    print("? - Sprawdź szacha")
    print("X - Wyjście z programu")

    wybor = input("Wybierz opcję: ").upper()

    if wybor == "0":
        rysuj(szachownica)

    elif wybor == "1":
        x = int(input("Podaj nr wiersza (1-8): "))
        y = int(input("Podaj nr kolumny (1-8): "))
        zmiana_w1(x - 1, y - 1)

    elif wybor == "2":
        x = int(input("Podaj nr wiersza (1-8): "))
        y = int(input("Podaj nr kolumny (1-8): "))
        zmiana_w2(x - 1, y - 1)

    elif wybor == "3":
        x = int(input("Podaj nr wiersza (1-8): "))
        y = int(input("Podaj nr kolumny (1-8): "))
        zmiana_h(x - 1, y - 1)

    elif wybor == "?":
        x = int(input("Podaj nr wiersza (1-8): "))
        y = int(input("Podaj nr kolumny (1-8): "))
        szach(x - 1, y - 1)

    elif wybor == "X":
        print("Zakończono działanie programu.")
        break

    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")
