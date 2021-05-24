"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re


def most_common_words(file_path, top_words):
    word_dict = {}

    with open(file_path, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip()

            for word in line.split():
                word = re.sub(r'\W+', '', word).lower()

                if word not in word_dict:
                    word_dict[word] = 0

                word_dict[word] += 1

    return sorted(word_dict.keys(), key=lambda x: word_dict[x], reverse=True)[:top_words]
