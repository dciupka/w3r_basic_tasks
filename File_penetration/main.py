# ilość słów, ilość znaków, iloś wierszy


def lines_counter(text):
    total = 0
    for line in text:
        if line !='\n':
            total += 1
    return {"liczba linijek": total}


def char_counter(text):
    total = 0
    for l in text:
        for ch in l:
            if ch != " " and ch !="\n":
                total += 1
    return {'chars': total}


def word_counter(text):
    total = 0
    for l in text:
        z=l.split()
        for w in z:
            total+=1
    return {"words":total}

file = 'PanTadeusz.txt'
with open(file, 'r', -1, "utf-8") as f:
    pan_tadeusz = f.readlines()
    print(file.__str__())
    print(char_counter(pan_tadeusz))
    print(word_counter(pan_tadeusz))
    print(lines_counter(pan_tadeusz))