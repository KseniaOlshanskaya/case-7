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
