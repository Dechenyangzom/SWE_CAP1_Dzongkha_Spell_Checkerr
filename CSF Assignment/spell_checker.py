import sys
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def load_dictionary(filtered_dictionary):
    # Detect encoding of the dictionary file
    encoding = detect_encoding(filtered_dictionary)
    print(f"Detected encoding for dictionary: {encoding}")

    # Load words from the dictionary with the detected encoding
    with open(filtered_dictionary, 'r', encoding=encoding) as f:
        dictionary = set(word.strip() for word in f.readlines())
    return dictionary

def spell_check(input_file, dictionary):
    # Read the Dzongkha text file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Iterate through each line
    for line_num, line in enumerate(lines, start=1):
        words = line.strip().split()
        # Check each word in the line
        for word_pos, word in enumerate(words, star):
            if word not in dictionary:
                # Print the error in the specified format
                print(f"line {line_num}, {word_pos}th word '{word}' is incorrect.")

def main():
    # Ensure that the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python dzongkha_spell_checker.py dzo.txt")
        return

    input_file = sys.argv[1]
    dictionary_file = 'filtered_dictionary.txt'  # Ensure this file is already cleaned and prepared

    # Load the dictionary and perform spell check
    dictionary = load_dictionary(dictionary_file)
    spell_check(input_file, dictionary)

if __name__== "_main_":
    main()