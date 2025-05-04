noteMath = float(input("Entrez la note de math: "))
noteInformatique = float(input("Entrez la note de informatique: "))
noteFrancais = float(input("Entrez la note de francais: "))

modules = [noteMath, noteInformatique, noteFrancais]
nom_modules = ["Mathématique", "Informatique", "Français"]

for i, note in enumerate(modules):
    if note >= 10:
        print(f"Le module {nom_modules[i]} est validé.")
    else:
        print(f"Le module {nom_modules[i]} est non validé.")
