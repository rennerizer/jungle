prompt = "Please enter the toppings you would like on your pizza (enter 'quit' when finished): "

toppings = []

topping = ""

while True:
    topping = input(prompt)

    if (topping == 'quit'):
        break
    else:
        toppings.append(topping)

print(f"your toppings: {toppings}")
