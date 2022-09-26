# -*- coding: utf-8 -*-
"""
Created on "13/09/2022"
@author: "Muhamad Abdul AZIZ"
"""


text = "I WENT AND CALLED, BUT GOT NO ANSWER. ON RETURNING, I WHISPERED TO CATHERINE THAT HE HAD HEARD A GOOD PART OF WHAT SHE SAID, I WAS SURE; ANDTOLD HOW I SAW HIM QUIT THE KITCHEN JUST AS SHE COMPLAINED OF HERBROTHER'S CONDUCT REGARDING HIM.  SHE JUMPED UP IN A FINE FRIGHT, FLUNG HARETON ON TO THE SETTLE, AND RAN TO SEEK FOR HER FRIEND HERSELF; NOT TAKING LEISURE TO CONSIDER WHY SHE WAS SO FLURRIED, OR HOW HER TALK WOULD HAVE AFFECTED HIM.  SHE WAS ABSENT SUCH A WHILE THAT JOSEPH PROPOSED WE SHOULD WAIT NO LONGER.  HE CUNNINGLY CONJECTURED THEY WERE STAYING AWAY IN ORDER TO AVOID HEARING HIS PROTRACTED BLESSING."

# letters
letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PROBLEM : find the occurence frequencies of the letters of the alphabet in the following text

# We can decompose the problem as follows :
#   1- create a dictionary containing the letters with the occurrences equal to 0 
letter_dict = {}
for letter in letters:
    letter_dict[letter] = 0

#   2- for each letter in the text, increment the corresponding entry of the dictionary
for char in text:
    for letter in letters:
        if char == letter:
            letter_dict[letter] += 1
          
#   3- normalize the values of the dictionary in order to have frequencies (the sum is equal to 1)
total_letter = 0
for key, value in letter_dict.items():
    total_letter += value

total_value = 0
for key, value in letter_dict.items():
    value = value / total_letter
    letter_dict[key] = value
    total_value += value

print(f"THe sum of frequencies: {total_value}")


