from random import randint
words = ['apple', 'orange', 'lemon', 'mango', 'lime', 'banana']


def ransengen(word):
    randomindex = randint(0, len(words)-1)
    return f'{words[randomindex]} {word}'


with open('./text.txt') as file:
    paragraph = file.read()
    wordlists = paragraph.split()
    sentencelist = list(map(ransengen, wordlists))
    paracount = int(input('How many paragraphs that you want? :'))

    for count in range(paracount):
        with open('./generator.txt', 'a') as writefile:
            writefile.write(''.join(sentencelist)+'\n\n')


