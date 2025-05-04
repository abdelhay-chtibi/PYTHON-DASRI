noteMath = float(input("Entrez la note de math: "))
noteInformatique = float(input("Entrez la note de informatique: "))
noteFrancais = float(input("Entrez la note de francais: "))
modules = [noteMath, noteInformatique, noteFrancais]
nom_modules = ["Mathematique", "Informatique", "Francais"]

# for i in range(len(modules)):
#     if modules[i] >= 10:
#         print(f"Le module {nom_modules[i]} est validé.")

for i in modules:
    j = modules.index(i)
    if i >= 10: 
        print("Le module", nom_modules[j], " est validé.")
    else: 
        print("Le module", nom_modules[j], " est non validé.")