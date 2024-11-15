import difflib

# Load the dictionary into a set
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines()) 

# Check if a word is in the dictionary
def check_spelling(word, dictionary):
    return word in dictionary

# Suggest corrections based on close matches
def suggest_corrections(word, dictionary):
    suggestions = difflib.get_close_matches(word, dictionary, n=3, cutoff=0.6)
    return suggestions

# Main function to run the spell checker on a given text
def spell_checker(text, dictionary):
    results = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        words = line.split()
        for position, word in enumerate(words, start=1):
            if not check_spelling(word, dictionary):
                suggestions = suggest_corrections(word, dictionary)
                result = {
                    'line_number': line_number,
                    'word_position': position,
                    'incorrect_word': word,
                    'suggestions': suggestions
                }
                results.append(result)
    return results

# Example usage
if __name__ == "__main__":
    dictionary = load_dictionary('filtered_dictionary.txt')
    
    # Sample text to check
    sample_text = """༉ ཀྲོང་གསར་ བྲ་སྟེང་རྒེད་འོག་གི་ ཀུན་དགའ་རབ་བརྟན་དང་ བསམ་ཆོས་གླིང་ཁ་སྨད་ཀྱི་མི་སེར་ལ་ལུ་ཅིག་ ད་ལྟོའི་བར་ན་ཡང་ ཁྱིམ་གྱི་གྱང་དང་འཐིང་གཞི་མེདཔ་བཏང་མི་ལུ་ རྒུད་འཐུས་ཐོབ་མ་འདི་ལུ་ སེམས་ང་མ་ལྡན་པར་འདུག

མི་ཚུ་གིས་སླབ་མི་ནང་ ཁོང་གི་ཁྱིམ་གྱི་གྱང་ཚུ་ཡང་ མང་སྡེ་ཆུ་གློག་མེ་ལས་འགུལ་འདི་གི་ ས་འོག་ལམ་འདི་ ཁོང་གི་གཡུས་ཀྱི་ཉེ་འདབས་ལུ་རང་ རྐྱབ་ནི་འདི་གིས་ བགག་གྲམ་ཕོག་སྟེ་ཡོདཔ་སྦེ་བཤད་ཅི།

ད་རུང་ ཁོང་གིས་སླབ་མི་ནང་ བགག་འགྲམ་ཚུ་ཡང་ སྤྱི་ལོ་༢༠༢༠ལུ་ མང་སུ་ཅིག་སྦེ་ ཐོན་ཏེ་ཡོདཔ་སྦེ་ཨིན་མས།

ཀྲོང་གསར་མང་སྡེ་ཆུ་གློག་མེ་ལས་གུལ་གྱིས་ སྤྱི་ལོ་༢༠༢༠ལུ་ བྲང་སྟེང་རྒེད་འོག་ནང་ལུ་ ཁྱིམ་བགག་གྲམ་ཕོག་མི་ ཁྱིམ་གུང་པ་༡༩ལུ་ རྒུད་འཐུས་ཚུ་སྤྲོད་ནུག

ཨིན་རུང་ ཁོང་མང་ཤོས་ཅིག་གིས་སླབ་མི་ནང་ འབྲེལ་ཡོད་ཡིག་ཚང་ཚུ་གིས་ ཞིབ་དཔྱད་འདི་ལོག་སྟེ་རང་འབད་ཞིནམ་ལས་ ཁོང་དང་གཅིག་ཁར་བསྟུན་གྲོས་འབད་དེ་ རྒུད་འཐུས་ཀྱི་ཐད་ཁར་ བསྐྱར་ཞིབ་འབད་དགོཔ་འདུག་ཟེར་བཤད་ཅི།

འདི་ལུ་ མང་སྡེ་ཆུ་གློག་མེ་ལས་འགུལ་གྱི་ འགོ་དཔོན་ཚུ་གིས་བཀོད་མི་ནང་ མི་སེར་ཚུ་ལུ་ རྒུད་འཐུས་ཚུ་ཡང་ འབྲལ་ཡོད་ལས་སྡེ་ཚུ་དང་གཅིག་ཁར་བསྟུན་གྲོས་འབད་དེ་རང་ སྤྲོད་ཡི་ཟེར་ཨིན་མས།

ད་རུང་ དབང་འཛིན་དི་དང་འཁྲིལ་བ་ཅིན ཁོང་གིས་ གནས་སྟངས་ཚུ་བལྟ་ཡི་ཟེར་ཨིནམ་མ་ཚད་ བལྟ་རྟོག་ཅ་ཆས་ཚུ་ཡང་བཙུགས་ཏེ་ཡོད་ུང་ ཁྱིམ་གུ་ལས་ཕར་ བགག་འགྲམ་འདི་ ནེ་ཅིག་ལས་བརྒལ་ མ་མཐོང་ཟར་བཤད་ཅི།

འདི་བཟུམ་སྦེ་ ལས་འགུལ་འདི་གི་ས་འོག་ལམ་འདི་ཡང་ རྟེན་གཞི་སྒྲིང་སྒྲི་འབད་རང་ཡོདཔ་སྦེ་ཨིན་མས།

འདི་དང་གཅིག་ཁར་ བྲག་སྟེང་རྒེད་འོག་ཡིག་ཚང་ནང་ལུ་ ཁྱིམ་འདི་ཚུ་དེ་སྦེ་བགག་གྲམ་ཕོག་སྟེ་ཡོདཔ་སྦེ་ ད་རུང་རང་ ཉོག་བཤད་ཁག་༡༡ལྷོད་དེ་ཡོདཔ་ཨིན་མས།

"""

    results = spell_checker(sample_text, dictionary)
    
    # Print results
    for result in results:
        print(f"Line {result['line_number']}, Position {result['word_position']}: "
              f"'{result['incorrect_word']}' is misspelled. Suggestions: {', '.join(result['suggestions']) if result['suggestions'] else 'No suggestions available.'}")