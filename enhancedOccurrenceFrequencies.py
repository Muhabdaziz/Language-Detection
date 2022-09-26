# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:20:08 2022

@author: Muhamad Abdul AZIZ
"""

# 1. Write a function readText...
def readText(location):
    infile = open(location)
    myText = infile.read()
    infile.close()
    
    myText = myText.lower()
    
    return myText

# 2. Apply this function to the...
myText = readText("data/wutheringHeights.txt")

# 3. Write a function to compute...
def occurrence_freq(characters, text):
    frequency_dist_dict = letter_counter(characters, text)
    
    # Calculate the total of letter
    letter_count = total_letter_counter(frequency_dist_dict)
    
    # Calculate the percentage of each letter
    for key, value in frequency_dist_dict.items():
        frequency_dist_dict[key] = value / letter_count
    
    return frequency_dist_dict

def letter_counter(characters, text):
    frequency_dist_dict = {}
    for character in characters:
        frequency_dist_dict[character] = 0
        
    for letter in text:
        for character in characters:
            if letter == character:
                frequency_dist_dict[character] += 1
                
    return frequency_dist_dict
    
def total_letter_counter(frequency_distribution):
    letter_count = 0
    for key, value in frequency_distribution.items():
        letter_count += value
        
    return letter_count

# 4. Apply this function to the string...
characters="abcdefghijklmnopqrstuvwxyz"
englishOF = occurrence_freq(characters, myText)

def write_output_file(dictionary, language):
    outfile = open("data/" + language + "OF.txt", mode="w")
    for letter, frequency in dictionary.items():
        outfile.write(letter + ";" + str(frequency) + '\n')
    
    outfile.close()
    
write_output_file(englishOF, "english")

# 5. Compute the occurrence frequencies of french, ...
frenchOF = occurrence_freq(characters, readText("data/MadameBovary.txt"))
spanishOF = occurrence_freq(characters, readText("data/donQuijote.txt"))
germanOF = occurrence_freq(characters, readText("data/kritikDerReinenVernunft.txt"))

write_output_file(frenchOF, "french")
write_output_file(spanishOF, "spanish")
write_output_file(germanOF, "german")

# 6 & 7. Create KL divergence calculator
from math import log, fabs
def KL_calc(P, Q):
    D_KL = 0
    for key, value in P.items(): # Here I already know that P.keys() == Q.keys()
        if Q[key] != 0 and P[key] != 0: # Get rid of the near-zero value of q
            D_KL +=  P[key] * log(P[key] / fabs(Q[key]), 2)
        
    return D_KL

def symmetric_KL(P, Q):
    D_KL_PQ = KL_calc(P, Q)
    D_KL_QP = KL_calc(Q, P)
    
    D_KL = fabs(D_KL_PQ + D_KL_QP) / 2
    
    return D_KL

# 8. Compute the KL divergence ...
languages = {"english" : englishOF, 
             "french" : frenchOF,
             "spanish" : spanishOF,
             "german" : germanOF}

tested = []
for language1 in languages.keys():
    for language2 in languages.keys():
        if language2 in tested:
            pass
        elif language2 == language1:
            pass
        else:
            D_KL = symmetric_KL(languages[language1], languages[language2])
            print(f"The KL divergence value between {language1} and {language2} is {round(D_KL,4)}")
    tested.append(language1)
        
# 9. Write a function "language detector" ...
def language_detector(text_location, characters, references):
    OF = occurrence_freq(characters, readText(text_location))
    
    KL_score = []
    KL_ref_list = []
    for key, value in references.items():
        D_KL = symmetric_KL(OF, references[key])
        KL_score.append(D_KL)
        KL_ref_list.append(key)
        
    # Find the minimum value of the KL Score 
    min_value = min(KL_score)
    loc = KL_score.index(min_value)
    
    return KL_ref_list[loc], min_value
    
# Test the function
test1, _ = language_detector("data/austen-emma.txt", characters, languages)
print(f"\nThe text1 is written in {test1}.")
test2, _ = language_detector("data/austen-emma-excerpt.txt", characters, languages)
print(f"The text2 is written in {test2}.")





# ---------- OPTIONAL PART ---------- 
# 4.1 Evaluate the prediction for different length of text
# separate text into each different length
separated_text = []
text_variation = range(500, 40000, 500)

# Calculate occurrence frequency
for i in text_variation:
    separated_text.append(occurrence_freq(characters, readText("data/austen-emma.txt")[0:i]))

# Calculate KL Divergence
KL_list = []
for text in separated_text:
    KL_list.append(symmetric_KL(text, languages["english"]))
    
# Plot
import matplotlib.pyplot as plt
plt.rc("text", usetex=True)
plt.rc("font", family="serif")

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(3,2), dpi=300)

ax.plot(text_variation, KL_list, "r", linestyle="solid")
ax.set_xlabel("Text Length")
ax.set_ylabel("KL Divergence")
ax.grid(linestyle="--")
ax.set_title("Detection quality for various text length")

# 4.2 To try improve this result, ...
import random

def new_letter_counter(characters, text, number_of_pairs, letter_in_pairs, exist_consecutive=False, consecutive=None):
    frequency_dist_dict = letter_counter(characters, text)
    
    frequency_dist_dict2 = {}
        
    # Random choice
    ref_char = "abcdefghijklmnopqrstuvwxyz" # Just to make sure the consecutive letters is in alphabet
    pairs = []
    if exist_consecutive:
        for key, value in consecutive.items():
            if len(key) > 1:
                frequency_dist_dict2[key] = 0
                
                for i in range(0, len(text) - 1):
                    if key == text[i] + text[i + 1]:
                        frequency_dist_dict2[key] += 1
                
    else:    
        random.seed(1000)
        # Choose random pairs
        for i in range(0, number_of_pairs):
            pairs.append("".join(random.sample(ref_char, letter_in_pairs)))
        
        for pair in pairs:
            frequency_dist_dict2[pair] = 0
            
        for pair in pairs:
            for i in range(0, len(text) - 1):
                if pair == text[i] + text[i + 1]:
                    frequency_dist_dict2[pair] += 1
    
    frequency_dist_dict.update(frequency_dist_dict2)
    
    return frequency_dist_dict

def new_occurrence_freq(characters, text, number_of_pairs, letter_in_pairs, exist_consecutive=False, consecutive=None):
    frequency_dist_dict = new_letter_counter(characters, text, number_of_pairs, letter_in_pairs, exist_consecutive, consecutive)
    letter_count = total_letter_counter(frequency_dist_dict)
    for key, value in frequency_dist_dict.items():
        frequency_dist_dict[key] = value / letter_count
        
    return frequency_dist_dict

# Test the program
text = readText("data/austen-emma.txt")
number_of_pairs = 10
letter_in_pairs = 2

englishOF2 = new_occurrence_freq(characters, text, number_of_pairs, letter_in_pairs)

separated_text_new = []
text_variation = range(500, 40000, 500)

# Calculate occurrence frequency
for i in text_variation:
    separated_text_new.append(new_occurrence_freq(characters, readText("data/austen-emma.txt")[0:i], 10, 2, True, englishOF2))

# Calculate KL Divergence
enhanced_KL_list = []
for text in separated_text_new:
    enhanced_KL_list.append(symmetric_KL(text, englishOF2))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(3,2), dpi=300)

ax.plot(text_variation, KL_list, "r", linestyle="solid", label="Standard")
ax.plot(text_variation, enhanced_KL_list, "green", linestyle="--", label="Enhanced")
ax.set_xlabel("Text Length")
ax.set_ylabel("KL Divergence")
ax.grid(linestyle="--")
ax.set_title("Detection quality for various text length")
ax.legend()