# Magic Potion Shop

# 1. Dictionary of potions and their ingredients

potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phonix feather", "troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

print("Welcome to the magic potion shop!\n")
print("Here are the potions you can chose from:\n")

# 2. Display the list of potions

for potion in potions:
    print("-", potion)

# Ask user to chose a potion
chosen_potion = input("\nWhich potion would you like to buy ingredients for? ")

# Check if the potion exists
if chosen_potion in potions:
    print(f"\nYou chose: {chosen_potion}")

    # Get the list of ingredients
    ingredients = potions[chosen_potion]

    print("\nThis potion requres the following ingredients: ")
    for item in ingredients:
        print("-", item)

    print("\nLet's start buying ingredients!\n")

    # 3. Use while loop to buy ingredients one by one

    index = 0 # start at the first ingredient

    while index < len(ingredients):
        next_item = ingredients[index]
        answer = input(f"Do you want to buy '{next_item}'? (yes/no): ").lower()

        if answer == "yes":
            print(f"You bought {next_item}!\n")
            index += 1 # move to the next ingredient
        else: 
            print("You stopped shopping early. Potion incomplete!")
            break
    

    # 4. If all the ingredients were purchased
    if index == len(ingredients):
        print(f"Success! You bought all ingredients for this {chosen_potion}!")
else:
    print("\nThat potion does not exist. Please restart the program.")