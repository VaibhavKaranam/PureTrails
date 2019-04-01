file = "trash_cans.txt"
file = open(file, "r")

coordinates = []

for line in file:
    new_words = []
    if '>' in line or '<' in line:
        continue
    else:
        words = line.split(" ")

    del words[0]
    for word in words:
        if ',' in word:
            word = word.replace(',', '')
            new_words.append(word)
        if '\n' in word:
            word = word.replace('\n', '')
            new_words.append(word)

    coords = (float(new_words[0]), float(new_words[1]))
    coordinates.append(coords)
