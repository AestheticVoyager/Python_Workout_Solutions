# DomirScire

def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),
                        second.get(key)]
    return output

if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d1,d2))
