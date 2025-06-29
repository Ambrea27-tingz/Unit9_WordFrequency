"""Name: Ambrea Williams
   
   Date: 06/29/2025

   Unit 9: Lab 9 - Coin Toss Game

   Description: This program counts the frequency of each word in a text file. 
   An let's the user choose a filename to read. 
   """
import string

def wordFreq(fptr):
    """Counts the frequency of each word in a text file.
    
    Args:
        fptr: A file pointer to the text file.
        
    Returns:
        A dictionary with words as keys and their frequencies as values.
    """
    freq = {}
    punct_chars = string.punctuation  # Using built-in punctuation list

    for line in fptr:
        line = line.strip()  # Remove leading/trailing whitespace
        for c in punct_chars:
            line = line.replace(c, "")  # Remove punctuation
        words = line.split()  # Split into words

        for word in words:
            word = word.lower()
            freq[word] = freq.get(word, 0) + 1  # Use get() method

    return freq