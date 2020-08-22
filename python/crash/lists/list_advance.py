pizzas = ['bacon', 'bbq chicken', 'tomato', 'four cheese']
for pizza in pizzas:
    print(f"this {pizza} pizza is fantastic")

print(f"I sure do like {len(pizzas)} pizzas")

#for number in range(1,21):
    #print(number)

#print(min(range(1,1000000)))

cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

cubes_tight = [value**3 for value in range(1,11)]
print(cubes_tight)