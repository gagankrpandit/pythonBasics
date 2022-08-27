# count top 20 words from text file
import operator

def word_count(filename):
    with open(filename, encoding="utf8") as f:
        speech = f.read()

    speech = speech.split(" ")
    print(f'Total words: {len(speech)}')
    unique_words = list(set(speech))
    
    dict_ = {}
    for i in range(len(unique_words)):
        dict_[unique_words[i]] = speech.count(unique_words[i])

    dict_ = dict((sorted(dict_.items(),key=operator.itemgetter(1),reverse=True))[:20])
    print('Top 20 Words\tFrequency')
    for k, v in dict_.items():
        print(f'{k}\t\t\t{v}')

word_count('speech_biden.txt')
