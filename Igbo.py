# Yoruba to English Dictionary (20 words)

yoruba_dictionary = { #by Matthew Folat
    "ẹ̀káàrọ̀": "Good morning",
    "ẹ̀káàsán": "Good afternoon",
    "ẹ̀káalẹ́": "Good evening",
    "báwo ni": "How are you?",
    "dáadáa ni": "I am fine",
    "orúkọ": "Name",
    "ilé": "House",
    "ọmọ": "Child",
    "ọrẹ́": "Friend",
    "ọkọ̀": "Husband",
    "iyàwó": "Wife",
    "ọbẹ̀": "Soup",
    "omi": "Water",
    "oúnjẹ": "Food",
    "ilé-ẹ̀kọ́": "School",
    "akẹ́kọ̀ọ́": "Student",
    "olùkọ́": "Teacher",
    "ìfẹ́": "Love",
    "ọlọ́run": "God",
    "ọjọ́": "Day"
}


english_to_igala = { #by Kamsi chukwumampkam
    "Hello": "Adoo",
    "Goodbye": "O dabo",
    "Thank you": "Ojo",
    "Please": "Joo",
    "Yes": "Ehe",
    "No": "Awo",
    "Man": "Ono",
    "Woman": "Iye",
    "Child": "Oma",
    "Food": "Eje",
    "Water": "Omi",
    "House": "Ile",
    "Road": "Ona",
    "Market": "Oja",
    "Money": "Owo",
    "Friend": "Ore",
    "Father": "Ata",
    "Mother": "Iya",
    "Morning": "Ojo-ola",
    "Night": "Ojo-ane"
}

nigerian_languages = {
    "Micheal": {  # Hausa
        "Language": "Hausa",
        "Words": {
            "Sannu": "Hello",
            "Nagode": "Thank you",
            "Eh": "Yes",
            "A'a": "No",
            "Ina kwana": "Good morning",
            "Ina wuni": "Good afternoon",
            "Ina yini": "Good evening",
            "Lafiya": "Fine / Health",
            "Ruwa": "Water",
            "Abinci": "Food",
            "Gida": "House",
            "Mutum": "Person",
            "Yaro": "Child",
            "Mace": "Woman",
            "Namiji": "Man",
            "Kudi": "Money",
            "Kasuwa": "Market",
            "Hanya": "Road",
            "Lokaci": "Time",
            "Aiki": "Work"
        }
    }
}

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




