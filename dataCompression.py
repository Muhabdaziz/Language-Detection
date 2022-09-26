# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:38:37 2022

@author: Muhamad Abdul AZIZ

"""

from enhancedOccurrenceFrequencies import *

characters = ""        
for i in range(128) : characters += chr(i)

englishOF_new = occurrence_freq(characters, readText("data/wutheringHeights.txt"))
frenchOF_new = occurrence_freq(characters, readText("data/MadameBovary.txt"))
spanishOF_new = occurrence_freq(characters, readText("data/donQuijote.txt"))
germanOF_new = occurrence_freq(characters, readText("data/kritikDerReinenVernunft.txt"))

def entropy_calc(probability_dist):
    H = 0
    for key, value in probability_dist.items():
        if value != 0:
            H += value * log(value, 2)
    
    return -1*H

# 2. Compute the entropies of french...

french_entropy = entropy_calc(frenchOF_new)
spanish_entropy = entropy_calc(spanishOF_new)
german_entropy = entropy_calc(germanOF_new)

print(f"\nCalculated French Entropy: {round(french_entropy, 4)}")
print(f"Calculated Spanish Entropy: {round(spanish_entropy, 4)}")
print(f"Calculated German Entropy: {round(german_entropy, 4)}")

# 4. Use these algorithm to compress and decompress...
print("\n-----Processing huffman compression-----")

from huffman import *
huff_tree_french = build_huffman_tree(frenchOF_new)
huff_tree_spanish = build_huffman_tree(spanishOF_new)
huff_tree_german = build_huffman_tree(germanOF_new)

encoding_dict_french = generate_code(huff_tree_french)
encoding_dict_spanish = generate_code(huff_tree_spanish)
encoding_dict_german = generate_code(huff_tree_german)

compressed_text_french = compress(readText("data/MadameBovary.txt"), encoding_dict_french)
compressed_text_spanish = compress(readText("data/donQuijote.txt"), encoding_dict_spanish)
compressed_text_german = compress(readText("data/kritikDerReinenVernunft.txt"), encoding_dict_german)

average_bits_french = len(compressed_text_french) / len(readText("data/MadameBovary.txt"))
average_bits_spanish = len(compressed_text_spanish) / len(readText("data/donQuijote.txt"))
average_bits_german = len(compressed_text_german) / len(readText("data/kritikDerReinenVernunft.txt"))

print(f"\nAverage bits per characters -french: {round(average_bits_french, 4)}")
print(f"Average bits per characters -spanish: {round(average_bits_spanish, 4)}")
print(f"Average bits per characters -german: {round(average_bits_german, 4)}")

print("\n-----Verifying entropy bound-----")
if (french_entropy < average_bits_french) and (spanish_entropy < average_bits_spanish) and (german_entropy < average_bits_german):
    print("\nMath is beautiful!")
    
print("\n-----Testing huffman decompression-----")
dec_dict = build_decoding_dict(encoding_dict_french)
decompressed_french = decompress(compressed_text_french, dec_dict)

if decompressed_french == readText("data/MadameBovary.txt"):
    print("\nBravo!")
else:
    print("\nIt's wrong")
    
print("\n-----Compression ratio-----")
compression_ratio_french = 7 / average_bits_french
compression_ratio_spanish = 7 / average_bits_spanish
compression_ratio_german = 7 / average_bits_german

print(f"\nCompression ratio -french: {round(compression_ratio_french, 6)}")
print(f"Compression ratio -spanish: {round(compression_ratio_spanish, 6)}")
print(f"Compression ratio -german: {round(compression_ratio_german, 6)}")

# 5. How to improve the level of compression? ...
# Try to capture redundancy
number_of_pairs = 50
letter_in_pairs = 2

print("\n-----Trying to improve the compression-----")
print("\nBe patient please :D")

frenchOF_new_enhanced = enhanced_occurrence_freq(characters, readText("data/MadameBovary.txt"), number_of_pairs, letter_in_pairs)
spanishOF_new_enhanced = enhanced_occurrence_freq(characters, readText("data/donQuijote.txt"), number_of_pairs, letter_in_pairs)
germanOF_new_enhanced = enhanced_occurrence_freq(characters, readText("data/kritikDerReinenVernunft.txt"), number_of_pairs, letter_in_pairs)

huff_tree_french_enhanced = build_huffman_tree(frenchOF_new_enhanced)
huff_tree_spanish_enhanced = build_huffman_tree(spanishOF_new_enhanced)
huff_tree_german_enhanced = build_huffman_tree(germanOF_new_enhanced)

encoding_dict_french_enhanced = generate_code(huff_tree_french_enhanced)
encoding_dict_spanish_enhanced = generate_code(huff_tree_spanish_enhanced)
encoding_dict_german_enhanced = generate_code(huff_tree_german_enhanced)

compressed_text_french_enhanced = compress(readText("data/MadameBovary.txt"), encoding_dict_french_enhanced)
compressed_text_spanish_enhanced = compress(readText("data/donQuijote.txt"), encoding_dict_spanish_enhanced)
compressed_text_german_enhanced = compress(readText("data/kritikDerReinenVernunft.txt"), encoding_dict_german_enhanced)

average_bits_french_enhanced = len(compressed_text_french_enhanced) / len(readText("data/MadameBovary.txt"))
average_bits_spanish_enhanced = len(compressed_text_spanish_enhanced) / len(readText("data/donQuijote.txt"))
average_bits_german_enhanced = len(compressed_text_german_enhanced) / len(readText("data/kritikDerReinenVernunft.txt"))

compression_ratio_french_enhanced = 7 / average_bits_french_enhanced
compression_ratio_spanish_enhanced = 7 / average_bits_spanish_enhanced
compression_ratio_german_enhanced = 7 / average_bits_german_enhanced

print(f"\nEnhanced compression ratio -french: {round(compression_ratio_french_enhanced, 6)}")
print(f"Enhanced compression ratio -spanish: {round(compression_ratio_spanish_enhanced, 6)}")
print(f"Enhanced compression ratio -german: {round(compression_ratio_german_enhanced, 6)}")

# 6. Compare Huffman with ArithmeticCoding and Lempel-Ziv
print("\n-----Processing ArithmeticCoding Compression-----")
from arith import *
radix = 2     
str = readText("data/MadameBovary.txt")
str = str.encode()
#enc, pow, freq = arithmethic_coding(str, str, radix)
#dec = arithmethic_decoding(enc, radix, pow, freq)
#print("%-25s=> %19s * %d^%s" % (str, enc, radix, pow))
    
''' NOTE: I have tested the ArithmeticCoding program but 
    it has a very high computational time to do the compression
    for MadameBovary text'''

print("\n-----Processing Lempel-Ziv-----")
from lzw import *
lzw_output = compressLZ(readText("data/MadameBovary.txt"))
#print(lzw_output)
lzw_decompress = decompressLZ(lzw_output)

if lzw_decompress == readText("data/MadameBovary.txt"):
    print("\nBravo!")
else:
    print("\nIt's wrong")

''' NOTE: LZW returns a different text after the decompression
    process, which maybe there is still some problems in the
    compression code'''