def tikrinti_laimejima(zaidejas):
    kombinacijos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for komb in kombinacijos:
        if lentele[komb[0]] == lentele[komb[1]] == lentele[komb[2]] == zaidejas:
            return True
    return False

x_laimejo = 0
o_laimejo = 0

vardas_x = input("Iveskite zaidejo X varda: ")
vardas_o = input("Iveskite zaidejo O varda: ")

kas_pradeda = "X"

while True:
    lentele = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dabartinis_zaidejas = kas_pradeda
    def atspausdinti_lentele():
        print(lentele[6], "|", lentele[7], "|", lentele[8])
        print("--+---+--")
        print(lentele[3], "|", lentele[4], "|", lentele[5])
        print("--+---+--")
        print(lentele[0], "|", lentele[1], "|", lentele[2])

    def ejimas(zaidejas):
        while True:
            vardas = vardas_x if zaidejas == "X" else vardas_o
            pasirinkimas = input(f"{vardas} {zaidejas}, pasirinkite langeli (1-9): ")

            if pasirinkimas in lentele:
                lentele[int(pasirinkimas)-1] = zaidejas
                break
            else:
                print("Blogas pasirinkimas. Bandyk dar karta.")

    for _ in range(9):
        atspausdinti_lentele()
        ejimas(dabartinis_zaidejas)

        if tikrinti_laimejima(dabartinis_zaidejas):
            atspausdinti_lentele()
            laimetojas = vardas_x if dabartinis_zaidejas == "X" else vardas_o
            print(f"Laimejo: {laimetojas} ({dabartinis_zaidejas})!")

            if dabartinis_zaidejas == "X":
                x_laimejo += 1
            else:
                o_laimejo += 1
            break

        if dabartinis_zaidejas == "X":
            dabartinis_zaidejas = "O"
        else:
            dabartinis_zaidejas ="X"

    else:
        atspausdinti_lentele()
        print("Lygiosios!")

    print(f"Statistika: {vardas_x} ({"X"}) {x_laimejo}, {vardas_o} ({"O"}) {o_laimejo}")

    darkarta = input("Dar karta??? (+/-)")
    if darkarta != "+":
        print("Viso gero.")
        break

    kas_pradeda = "O" if kas_pradeda == "X" else "X"