from random import randint


def words(text, sentanse):
    """Function for word separating"""
    word = ""
    finish_words = []
    start_words = []
    list_of_words = []
    for i in text:
        if i != " ":
            word += i
        else:
            list_of_words.append(word)
            word = ""

    for i in list_of_words:
        for n in i:
            if n == "." or n == "?" or n == "!":
                finish_words.append(i)
        else:
            pass

    for i in list_of_words:
        if i.istitle():
            start_words.append(i)
    dictionary(list_of_words, start_words, finish_words, sentanse)


def dictionary(list_of_words, start_words, finish_words, sentanse):
    """ Function for dictionary """
    d = []
    for i in range(len(list_of_words)):
        if list_of_words[i] not in finish_words:
            d.append(list_of_words[i])
    a = []
    c = []
    b = {}
    for i in range(len(d)):
        if d[i] not in c:
            while d[i] in list_of_words:
                k = list_of_words.index(d[i])
                a.append(list_of_words[k + 1])
                list_of_words.pop(k)
                b.update({d[i]: a})
            a = []
            c.append(d[i])
        else:
            pass
    text(b, start_words, sentanse, finish_words)
