# Sample dictionary (a sorted list of words)
dictionary = [
    "apple",
    "banana",
    "cherry",
    "grape",
    "orange",
    "strawberry",
    "watermelon",
]

def binary_search(word, dictionary):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        current_word = dictionary[mid]

        if current_word == word:
            return True  # Word found in the dictionary
        elif current_word < word:
            low = mid + 1
        else:
            high = mid - 1

    return False  # Word not found in the dictionary

def main():
    while True:
        print("\nDictionary Search & Spell Checker")
        print("1. Search for a word")
        print("2. Spell check a word")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            search_word = input("Enter a word to search for: ")
            if binary_search(search_word, dictionary):
                print(f"'{search_word}' is in the dictionary.")
            else:
                print(f"'{search_word}' is not in the dictionary.")
        
        elif choice == "2":
            spell_check_word = input("Enter a word to spell check: ")
            if binary_search(spell_check_word, dictionary):
                print(f"'{spell_check_word}' is spelled correctly.")
            else:
                print(f"'{spell_check_word}' might be misspelled.")
        
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
