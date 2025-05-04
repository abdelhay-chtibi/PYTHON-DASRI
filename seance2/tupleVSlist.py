# Liste
etudiants = ["Ahmed", "Sara"]
etudiants.append("Yassine")  # possible
print(etudiants)

# Tuple
coordonnees = (34.05, -118.25)
print(coordonnees)
# coordonnees[0] = 35.0  ❌ Erreur ! tuple non modifiable

print("------------------------------------------")
ma_liste = [1, "abdelhay", 13, True]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[-2])
print(ma_liste[-3])


print("------------------------------------------")
ma_liste1 = [1, "abdelhay", 13, True,1 ,2 ,3, 4, None]
#start:end:step
test = ma_liste1[1::2]
print(test)


print("------------------------------------------")
ma_liste2 = [1, "abdelhay", 13, True,1 ,2 ,3, 4, None]
ma_liste2[0] = 11111
print(ma_liste2)

print("------------------------------------------")
mon_tuple = (1, "abdelhay", 13, True,1 ,2 ,3, 4, None)
# mon_tuple[0] = 11111 # tuple n'est pas modifiable 
print(mon_tuple)

print("------------------------------------------")
full_name = "Abdelhay chtibi"
print(full_name[2:8:2])
# full_name[5] = "E" # les chaine de caractere ne sont pas modifiable 
print(full_name)



