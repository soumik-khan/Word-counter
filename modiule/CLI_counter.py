import os
import re
from collections import Counter
from PyPDF2 import PdfFileReader
from docx import Document

def count_words(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PdfFileReader(file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page_num).extractText()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = ''
        for para in doc.paragraphs:
            text += para.text

    # Remove non-alphanumeric characters and convert text to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

    # Split text into words
    words = text.split()

    # Count the total number of words
    total_words = len(words)

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Calculate the percentage of each word
    word_percentages = {word: (count / total_words) * 100 for word, count in word_counts.items()}

    return word_counts, word_percentages

def main(file_path):
    if os.path.exists(file_path):
        word_counts, word_percentages = count_words(file_path)
        print("Word counts:")
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count} ({word_percentages[word]:.2f}%)")
        return word_counts, word_percentages
    else:
        print("File not found.")
        return None, None

if __name__ == "__main__":
    file_path = input("Enter the path of the file (.txt, .pdf, or .docx): ")
    main(file_path)
