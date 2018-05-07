import codecs
import re
import matplotlib.pyplot as plt


def count_words(text):
    #p = re.compile("(\W*\d+(\W\d+)*\W*)|((\W)*([a-zA-Z]\.){2,}(\W)*)|([^\w'/-]+)|(\W+[-'])|([-']\W+)|((\W*\/)(?!DC))")
    #stext = re.split(p, text)
    #stext = [value for value in stext if value is not None and value != ' ']

    stext = text.split()
    print(stext)


def count_unique_words(text):
    raw_string = re.split(re.compile("[\\W]|[0-9]"), text.lower())
    word_map = {}
    for word in raw_string:
        word_map[word] = word_map.get(word, 0) + 1
    print("Unique words found: " + str(len(word_map)) + "\n")


def frequency_distribution(text):
    raw_string = re.sub(r'[\W0-9]+', '', text.lower())
    char_map = {}
    for char in raw_string:
        char_map[char] = char_map.get(char, 0) + 1
    for char, count in sorted(char_map.items()):
        print("{}: {}".format(char, count))
    plot(sorted(char_map.items()))


def plot(lists):
    x, y = zip(*lists)
    plt.bar(x, y, width=0.5)
    plt.show()


if __name__ == '__main__':
    text = codecs.open('data.txt', encoding='utf-8', mode='r').read()
    print(text)
    count_words(text)
    count_unique_words(text)
    frequency_distribution(text)
