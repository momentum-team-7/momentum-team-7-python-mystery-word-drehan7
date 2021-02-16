import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    regex = re.compile("[^a-zA-Z]")
    with open(file, 'r') as f:
        file_words_list = f.read().split()

    lowercase_wordlist = []
    for word in file_words_list:
        lowercase_wordlist.append(regex.sub('', word).lower())

    for word in lowercase_wordlist:
        for stopword in STOP_WORDS:
            if word == stopword:
                lowercase_wordlist.remove(word)

    frequency_dict = {}
    for word in lowercase_wordlist:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    for k, v in frequency_dict.items():
        print("{:>16} | {:<3} {:<5}".format(k, v, ('*'*v)))


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
