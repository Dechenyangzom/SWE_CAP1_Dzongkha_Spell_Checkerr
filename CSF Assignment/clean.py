# Define the function to remove characters which are in english
def removing_english_characters_from_dictionary(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        contents = infile.readlines()

    # Define a list to hold lines without English characters
    filtered_lines = []

    for line in contents:
        # Keep only non-English characters (anything not a-z or A-Z)
        filtered_line = ''.join(filter(lambda char: not char.isascii(), line))
        filtered_lines.append(filtered_line)

    # Write the filtered lines to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(filtered_lines)

# Usage
input_file = 'dictionary.txt'  # replace with your input file
output_file = 'filtered_dictionary.txt'  # replace with desired output file
removing_english_characters_from_dictionary(input_file, output_file)