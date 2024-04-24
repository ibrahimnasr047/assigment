import re
from collections import Counter
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Function to read file contents
def read_file(filename):
    with open(r"D:\docker assigment\random_paragraphs.txt", 'r') as file:
        return file.read()

# Function to remove stopwords from text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Function to count word frequency
def count_word_frequency(words):
    return Counter(words)

# Function to display word frequency count
def display_word_frequency(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

# Main function
def main(filename):  # Accepts filename as an argument
    text = read_file(filename)
    words = remove_stopwords(text)
    word_freq = count_word_frequency(words)
    display_word_frequency(word_freq)

if __name__ == "__main__":
    main(r"D:\docker assigment\random_paragraphs.txt")