import re

def word_count(phrase):
    words = re.findall(r"[a-zA-Z\d']+", phrase)
    count = dict()
    for word in words:
        if count.get(word.lower())!=None:
            count.update({word.lower() : count.get(word.lower()) + 1})
        else:
            count[word.lower()] = 1
    return count

if __name__ == "__main__":
    word_count("First: don't laugh. Then: don't cry.")
