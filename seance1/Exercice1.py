montant = 1554
enfant = 9
partPourChaqueEnfant = montant // enfant
reste = montant % 9
print("La part de chaque enfant: ",partPourChaqueEnfant)
print("Il reste ", reste, "pieces")
print((partPourChaqueEnfant * enfant ) + reste)