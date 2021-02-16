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
        lowercase_wordlist.append(regex.sub('', word.lower()))
        if word in STOP_WORDS:
            lowercase_wordlist.pop(lowercase_wordlist.index(word))
    print(lowercase_wordlist)

    frequency_dict = {}
    for result in lowercase_wordlist:
        if result in frequency_dict:
            frequency_dict[result] += 1
        else:
            frequency_dict[result] = 1

    for k, v in sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True):
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
