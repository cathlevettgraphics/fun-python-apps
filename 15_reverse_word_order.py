# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

words = input('give me words and I will reverse them! ')


def reverse_words(w):
    return ' '.join(w.split()[::-1])

print(reverse_words(words)) 

