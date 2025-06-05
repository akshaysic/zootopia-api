import data_fetcher

def main():
    preset_animals = ["Cat", "Dog", "Fox", "Lion", "Elephant", "Monkey", "Tiger"]

    while True:
        print("Choose an option:")
        print("1. Select from a list")
        print("2. Type an animal name")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            for i, animal in enumerate(preset_animals, start=1):
                print(f"{i}. {animal}")
            selected = input("Enter the number of the animal: ")
            if selected.isdigit() and 1 <= int(selected) <= len(preset_animals):
                animal_name = preset_animals[int(selected) - 1]
                break
            else:
                print("Invalid number. Try again.\n")
        elif choice == "2":
            animal_name = input("Enter a name of an animal: ").strip()
            if animal_name:
                break
            else:
                print("Please enter a valid name.\n")
        else:
            print("Invalid option. Try again.\n")

    while True:
        animals = data_fetcher.fetch_data(animal_name)
        if animals:
            animals = animals[:10]
            break
        else:
            print(f'Sorry, no results for "{animal_name}". Try again.\n')
            animal_name = input("Enter a name of an animal: ").strip()

    with open("animals.html", "w") as f:
        f.write("<html><head><title>Zootopia Results</title>\n")
        f.write("<style>\n")
        f.write("body { font-family: Arial; margin: 20px; }\n")
        f.write("section { border: 1px solid #ccc; padding: 10px; margin-bottom: 15px; border-radius: 8px; }\n")
        f.write("h1 { color: #2c3e50; }\n")
        f.write("h2 { color: #16a085; }\n")
        f.write("</style>\n</head><body>\n")
        f.write(f"<h1>Animal Search: {animal_name}</h1>\n")

        for animal in animals:
            f.write("<section>\n")
            f.write(f"<h2>{animal.get('name', 'Unknown')}</h2>\n")
            c = animal.get('characteristics', {})
            f.write(f"<p><strong>Diet:</strong> {c.get('diet', 'Unknown')}</p>\n")
            f.write(f"<p><strong>Habitat:</strong> {c.get('habitat', 'Unknown')}</p>\n")
            f.write(f"<p><strong>Top Speed:</strong> {c.get('top_speed', 'Unknown')}</p>\n")
            f.write("</section>\n")

        f.write("</body></html>")

    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()
