a = float(input("Entrez la valeur de a: "))
b = float(input("Entrez la valeur de b: "))
c = float(input("Entrez la valeur de c: "))

if a == 0:
    if b == c:
        print("Infinité de solutions.")
    else:
        print("Pas de solution.")
else:
    result = (c - b) / a
    print(f"Le résultat de l'équation {a}x + {b} = {c} est : x = {result}")
