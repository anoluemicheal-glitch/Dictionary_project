# Translational Igbo ↔ English Dictionary

dictionary = {
    "ndeewo": "hello",
    "kedu": "how are you",
    "biko": "please",
    "daalu": "thank you",
    "nnoo": "welcome",
    "mmiri": "water",
    "nri": "food",
    "ulo": "house",
    "aku": "wealth",
    "ala": "land",
    "ego": "money",
    "akwukwo": "book",
    "nwoke": "man",
    "nwanyi": "woman",
    "nwa": "child",
    "ubochi": "day",
    "abali": "night",
    "enyi": "friend",
    "azu": "fish",
    "anya": "eye"
}

# Create reverse dictionary (English → Igbo)
reverse_dictionary = {value: key for key, value in dictionary.items()}

print("IGBO ↔ ENGLISH TRANSLATOR")
print("1. Igbo to English")
print("2. English to Igbo")

choice = input("Choose translation (1 or 2): ")

if choice == "1":
    word = input("Enter Igbo word: ").lower()
    if word in dictionary:
        print("Meaning:", dictionary[word])
    else:
        print("Word not found.")

elif choice == "2":
    word = input("Enter English word: ").lower()
    if word in reverse_dictionary:
        print("Igbo word:", reverse_dictionary[word])
    else:
        print("Word not found.")

else:
    print("Invalid choice.")
