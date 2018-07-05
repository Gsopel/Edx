def spelling_corrector(sentence, correct_spells):
    words = sentence.strip().lower().split()
    correct_lower = [cs.lower() for cs in correct_spells]
    result = [correction(w, correct_lower) for w in words]
    return ' '.join(result)

def replace_1(bad, good):
    if len(bad) != len(good):
        return False

    changes = 0
    for i,ch in enumerate(bad):
        if ch != good[i]:
            return bad[i+1:] == good[i+1:]

    return False

def insert_1(bad, good):

    if len(bad) != len(good) - 1:
        return False

    for i,ch in enumerate(bad):
        if ch != good[i]:
            return bad[i:] == good[i+1:]

    # At this point, all of bad matches first part of good. So it's an
    # append of the last character.
    return True

def delete_1(bad, good):
    """Return True if bad can be converted to good by deleting 1 letter.
    """
    if len(bad) != len(good) + 1:
        return False
    return insert_1(good, bad)


def correction(word, correct_spells):
    if len(word) < 3:
        return word
    if word in correct_spells:
        return word
    for good in correct_spells:
        if replace_1(word, good):
            return good
        if insert_1(word, good):
            return good
        if delete_1(word, good):
            return good

    return word

tests = (
    ('Thes is the Firs cas', "that first case car", 'thes is the first case'),
    ('programming is fan and easy', "programming this fun easy hook", 'programming is fun and easy'),
    ('Thes is vary essy', "this is very very easy", 'this is very easy'),
    ('Wee lpve Python', "we Live In Python", 'we live python'),)

if __name__ == "__main__":
    for t in tests:
        correct = t[1].split()
        print(t[0], "|", t[1], "|", t[2])
        print("Result:", spelling_corrector(t[0], correct))
        assert spelling_corrector(t[0], correct) == t[2]




