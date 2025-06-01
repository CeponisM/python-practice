# ### 4. Word Frequency Counter

# **Description**: Analyze text files and count word occurrences.

# **Practice Goals**:
# - Text file processing
# - Dictionary usage for data counting
# - Data sorting and display

import os

print("Word count text processor.")

def check_file():
    filename = input("Enter file name: ")
    word_count_dict = {}

    # Check if file exists
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            text = file.read()

            # Split text into words
            words = text.split()

            # Count each word
            for word in words:
                # Strip punctuation and make lowercase
                word = word.lower().strip(".,!?\"';:-()[]{}")

                if word:  # make sure word is not empty
                    if word in word_count_dict:
                        word_count_dict[word] += 1
                    else:
                        word_count_dict[word] = 1

        # Sort dictionary by frequency (highest first)
        sorted_words = sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)

        # Display results
        print("\nWord Frequencies:")
        for word, count in sorted_words:
            print(f"{word}: {count}")

        if input("Check other files (y/n)? ").lower() in ['y', 'yes']:
            check_file()
        else:
            return

    else:
        print("File does not exist.")
        check_file()

check_file()