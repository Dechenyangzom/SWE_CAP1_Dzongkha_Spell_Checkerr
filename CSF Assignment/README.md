# https://github.com/Dechenyangzom/SWE_CAP1_Dzongkha_Spell_Checkerr



## Dechen Yangzom
## 02240338


# REFERENCES

## https://openai.com
## https://cloudconvert.com
## https://www.tabnine.com



# SOLUTION

# Dzongkha Spell Checker

## Project Overview
The Dzongkha Spell Checker is a comprehensive project aimed at improving the accuracy and consistency of written Dzongkha. This project combines a robust dictionary cleaning tool with a spell-checking mechanism to support writers, educators, and language enthusiasts in producing high-quality Dzongkha text.



## Table of Contents

1.Usage   
2.Implementation   
3.Data Strucutures    
4.Algorithms   
5.Challenges and Solutions  
6.Future Improvements   
7.References



## 1.Usage

The Dzongkha Spell Checker project consists of two main components: 

1.the Dictionary Cleaner 

2.the Spell Checking Algorithm




## 2. Implementation

The Dzongkha Spell Checker project is implemented in Python and consists of two main components:  

1.the Dictionary Cleaner   

2.the Spell Checking Algorithm. 





## Data Structures

The Dzongkha Spell Checker project utilizes several data structures to efficiently store and process the dictionary and perform spell checking. 

### Set for Dictionary Storage

The cleaned Dzongkha dictionary is stored in memory using a Python set data structure.


### List for Suggestion Storage
When generating spelling suggestions, a Python list is used to store potential corrections.





## Algorithms

The Dzongkha Spell Checker employs several algorithms to perform its core functionalities. 

### Dictionary Cleaning Algorithm

This algorithm is used to preprocess the raw dictionary file and remove non-Dzongkha characters.


### Spell Checking Algorithm
This algorithm checks if a given word is present in the dictionary.


### Suggestion Generation Algorithm
For misspelled words, this algorithm generates potential corrections. It uses a combination of techniques:




## Performance Analysis

The performance of the Dzongkha Spell Checker is crucial for its practical application. This section provides an overview of the performance characteristics of the main components and algorithms used in the project.

###  Dictionary Loading

The initial loading of the dictionary is a one-time operation that affects the startup time of the spell checker.


### Spell Checking

The core spell-checking operation is highly efficient due to the use of a Set data structure.

### Suggestion Generation

Generating suggestions for misspelled words is the most computationally intensive part of the spell checker.

### Memory Usage

The memory footprint of the spell checker is primarily determined by the size of the dictionary.


## Challenges and Solutions

The development of the Dzongkha Spell Checker presented several unique challenges due to the nature of the Dzongkha language and the complexity of natural language processing. Here are some of the main challenges we encountered and the solutions we implemented:

### 1. Limited Digital Resources for Dzongkha

Challenge: 

Dzongkha, being a less-digitized language, lacks extensive digital resources such as comprehensive dictionaries and large text corpora.

Solution: 
- Collaborated with Dzongkha language experts to create and validate a custom Dzongkha dictionary.
- Implemented web scraping tools to collect Dzongkha text from available online sources to expand our dataset.
- Encouraged community contributions to continuously improve and expand the dictionary.

### 2. Complex Writing System

Challenge:      

Dzongkha uses the Tibetan script, which has a complex writing system with many stacked characters and special rules.

Solution:
- Developed custom string processing functions to handle Dzongkha's unique character combinations.
- Implemented special rules in the spell-checking algorithm to account for valid character stacks and combinations.

### 3. Lack of Standardized Spelling

Challenge:      

 Dzongkha, like many languages, has variations in spelling for certain words, making it difficult to determine correct spellings definitively.

Solution:
- Included common spelling variations in the dictionary.
- Implemented a suggestion system that proposes multiple valid spellings when applicable.
- Allowed for user customization to add preferred spellings to a personal dictionary.

### 4. Phonetic Similarities

Challenge:      

Many Dzongkha words sound similar but are spelled differently, making it challenging to provide accurate suggestions for misspelled words.

Solution:
- Developed a custom phonetic algorithm for Dzongkha to encode words based on their pronunciation.
- Incorporated phonetic similarity checks in the suggestion generation process to improve the relevance of suggestions.

### 5. Performance with Large Dictionaries

Challenge:    

As the dictionary grew, the performance of spell-checking and suggestion generation slowed down.

Solution:
- Implemented more efficient data structures like Sets for faster lookups.
- Optimized the Levenshtein distance algorithm with early termination conditions.
- Introduced caching mechanisms for frequently checked words and their suggestions.






## Future Performance Improvements

1. Implement more efficient data structures like Trie for faster prefix-based operations.
2. Optimize the suggestion generation algorithm to reduce the number of comparisons.
3. Implement a custom Dzongkha phonetic algorithm to improve suggestion accuracy and potentially reduce the need for extensive edit distance calculations.
4. Consider using machine learning techniques for more intelligent suggestion ranking.



## References
### Chat gpt
### Tabnine ai
### Cloudcovert
### codeacademy
 
