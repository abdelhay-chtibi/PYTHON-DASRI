noteMath = float(input("Entrez la note de math: "))
noteInformatique = float(input("Entrez la note de informatique: "))
noteFrancais = float(input("Entrez la note de francais: "))

if noteMath >= 10 : 
    print("module MATH validé.")
else:
    print("module non validé.")
    
if noteInformatique >= 10 : 
    print("module INFORMATIQUE validé.")
else:
    print("module non validé.")

if noteFrancais >= 10 : 
    print("module FRANCAIS validé.")
else:
    print("module non validé.")

moyenne = .5 * noteMath + .4 * noteInformatique + .1 * noteFrancais
print("Votre moyenne est: ", moyenne)

if moyenne >= 18:
    print("EXcellent.")
elif moyenne >=16:
    print("Tres bien.")
elif moyenne >=14:
    print("Tres bien.")
elif moyenne >=12:
    print("Passable.")
else:
    print("non validé.")