def lire_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un entier valide.")

def resoudre_equation(a, b, c):
    print(f"\nRésolution de l'équation : {a}x + {b} = {c}")

    if a == 0:
        if b == c:
            print("Cette équation a une infinité de solutions.")
        else:
            print("Cette équation n'a pas de solution.")
    else:
        x = (c - b) / a
        print(f"Solution unique : x = {x}")

def main():
    while True:
        print("\n--- Solveur d'équation du 1er degré ---")
        a = lire_entier("Entrez la valeur de a : ")
        b = lire_entier("Entrez la valeur de b : ")
        c = lire_entier("Entrez la valeur de c : ")

        resoudre_equation(a, b, c)

        choix = input("\nVoulez-vous résoudre une autre équation ? (o/n) : ").lower()
        if choix != 'o':
            print("Merci d'avoir utilisé le solveur !")
            break

main()
