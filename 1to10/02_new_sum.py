# DomirScire

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

if __name__ == "__main__":
    print(mysum(10, 20, 30, 40))
