ma_liste = [ 1, 5, 18181, 55, 100]

somme_avec_sum = sum(ma_liste)
print(somme_avec_sum)

sum = 0
for i in ma_liste:
    sum = sum + i

print(sum)

test_somme = somme_avec_sum == sum
print(test_somme)