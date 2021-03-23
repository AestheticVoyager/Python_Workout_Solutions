# DomirScire

def flipped_dict(a_dict):
    return {value: key
            for key, value in a_dict.items()}

if __name__ == "__main__":
    print(flipped_dict({'a':1, 'b':2, 'c':3}))
