def sub_search(word, val):
    len1 = len(val)
    if len1 != 0:
        word1 = word.split()
        new_word = ""
        try:
            for i in range(len1):
                new_word += word1[val[i]-1] + " "
            return new_word.strip()
        except:
            return new_word
    else:
        return word.strip()

def search(filename, word, cs = "a", w = [], ht = [0,0], th = [0,0]):
    final = ""
    with open(filename, "r") as file:
        if cs == "i":
            word = word.lower()
            for i in file:
                if word in i.lower():
                    final += sub_search(i, w) + "\n"

        else:
            for i in file:
                if word in i:
                    final += sub_search(i, w) + "\n"

    final = final.strip()

    if ht != []:
        if ht[0] > 0:
            final = head(final, ht[0])
        if ht[1] > 0:
            final = tail(final, ht[1])

    if th != []:
        if th[0] > 0:
            final = tail(final, th[0])
        if th[1] > 0:
            final = head(final, th[1])

    return final

def head(val, n):
    val = val.split('\n')
    val1 = ""
    for i in range(n):
        val1 += val[i] + '\n'
    return val1.strip()

def tail(val, n):
    val = val.split('\n')
    val1 = ""
    for i in range(-n, 0):
        val1 += val[i]+'\n'
    return val1.strip()

def help():
    print("search(filename,search_word,cs,w,ht/th)\n\tcs = 'i' - ignore case sensitive search\n\tw = [1,2,....,n] - print the words in a row (index starts from 1)\n\tht = [head, tail] - head and tail values (index starts from 1)\n\tth = [tail, head] - tail and head values (index starts from 1)")
    return ""
