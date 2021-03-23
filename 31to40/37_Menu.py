# DomirScire

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(
            f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        print('Not a valid option')

def func_a():
    return "A"

def func_b():
    return "B"

if __name__ == "__main__":
    return_value = menu(a=func_a, b=func_b)
    print(f'Result is {return_value}')
