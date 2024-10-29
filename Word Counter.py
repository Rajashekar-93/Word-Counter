def count_words(text):
    """
    Counts the number of words in a given text.
    A word is defined as a sequence of characters separated by whitespace or punctuation.
    """
    words = text.split()  # Split the text by whitespace
    return len(words)

def main():
    """
    Main function to prompt the user, process the input, and display the word count.
    """
    # Prompt user for input
    text = input("Please enter a sentence or paragraph: ").strip()
    
    # Check for empty input
    if not text:
        print("Error: No text entered. Please provide a valid sentence or paragraph.")
        return
    
    # Count the words and display the result
    word_count = count_words(text)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
