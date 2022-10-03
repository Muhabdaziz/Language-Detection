# Language-Detection

The aim of this project is to analyze a text in order to detect its language. 
The idea is to find the occurrence frequencies of the characters in the text. 
These frequecies are considered as probability distribution and will be used for several purposes:

1. Detect the language of a text by comparing its probability distribution with several distribution 
probabilities of languages (english, french, spanish, and germany).
2. Compress a text by using Huffman algorithm.

The main code of this project is called "enhancedOccurrenceFrequencies.py" and the simplified version is "occurrenceFrequencies.py" (Only for calculating the probability distribution). 
In this code, a theorem called Kullback-Leibler (KL) divergence is used to identify the information loss between two probability distributions.

For the text compression, Huffman method is used. Also, a mathematical concept called entropy is also used to obtaine a bound on the average number of bits used to code a symbol. Then, this entropy concept is validated using Huffman method.
