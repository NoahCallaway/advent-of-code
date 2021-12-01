file_path = "test-input.txt"
data = open(file_path)

ingredients = []
allergens = []

for line in data:
    ing, aller = line[:-1].replace(')','').split(' (contains ')
    ingredients.append(set(ing.split()))
    allergens.append(set(aller.split(', ')))

all_alergens = set.union(*allergens)

valid = set.union(*( set.intersection(*(
    ing for ing,al in zip(ingredients,allergens) if allergen in al
)) for allergen in all_alergens))

count = 0 
for i in ingredients:
    count += len(i-valid)
print("Part1:",count)
