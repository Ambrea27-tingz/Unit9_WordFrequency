"""Name: Ambrea Williams
   
   Date: 06/29/2025

   Unit 9: Lab 9 - Coin Toss Game

   Description: This program counts the frequency of each word in a text file. 
   An let's the user choose a filename to read. 
   """
import string
from pathlib import Path

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

def printWds(data):
    """Prints the words and their frequencies in alphabetical order.
    
    Args:
        data: A dictionary with words as keys and their frequencies as values.
    """
    print("\nWord Frequency:\n")
    for word in sorted(data.keys()):
        print(f"{word}: {data[word]}")

def main():
    """Main function to execute the word frequency counting."""
    
    while True:
        file_name = input("Enter the file name (or 'exit' to quit): ")

        if file_name.lower() == 'exit':
            print("Exiting program.")
            break

        path = Path(file_name)  # NEW

        if path.is_file():  # NEW check
            with path.open('r') as file:  # NEW
                print(f"File '{file_name}' has been successfully read.\n")
                word_counts = wordFreq(file)
                printWds(word_counts)
        else:
            print("File not found. Please make sure the file exists.")

if __name__ == "__main__":
    main()