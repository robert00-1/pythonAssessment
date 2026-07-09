from collections import Counter
import string
import re


with open("news_article.txt", "r", encoding="utf-8") as file:
    article = file.read()



def count_specific_word(text, search_word):
    words = []

    for word in text.lower().split():
        clean_word = word.strip(string.punctuation)
        words.append(clean_word)

    return words.count(search_word.lower())



def identify_most_common_word(text):
    if text == "":
        return None

    words = text.lower().split()
    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]



def calculate_average_word_length(text):
    if text == "":
        return 0

    words = text.split()

    total_length = 0
    total_words = 0

    for word in words:
        clean_word = word.strip(string.punctuation)

        if clean_word:
            total_length += len(clean_word)
            total_words += 1
    if total_words == 0:
        return 0    

    return total_length / total_words



def count_paragraphs(text):
    if text == "":
        return 1

    paragraphs = text.split("\n\n")

    return len(paragraphs)



def count_sentences(text):
    if text == "":
        return 1

    sentences = re.split(r"[.!?]+", text)
    sentences = [sentence for sentence in sentences if sentence.strip()]

    return len(sentences)

if __name__ == "__main__":

    while True:
        word = input("Enter a word to search (or type 'quit' to exit): ")

        if word.lower() == "quit":
            break

        count = count_specific_word(article, word)

        if count == 0:
            print("Word not found.")
        else:
            print("Occurrences:", count)

    print("\nText Analysis Results")
    print("----------------------")
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", calculate_average_word_length(article))
    print("Number of paragraphs:", count_paragraphs(article))
    print("Number of sentences:", count_sentences(article))