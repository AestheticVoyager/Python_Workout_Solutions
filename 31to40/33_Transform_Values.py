# DomirScire

def transfrom_values(func, a_dict):
    return {key:func(value)
            for key, value in a_dict.items()}

if __name__ == "__main__":
    d = {'a':1, 'b':2, 'c':3}
    print(transfrom_values(lambda x: x*x, d))
