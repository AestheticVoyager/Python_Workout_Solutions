# DomirScire

def pl_sentence(sentence):
    output=[]
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

if __name__ == "__main__":
    print(pl_sentence('This is a stupid test'))
