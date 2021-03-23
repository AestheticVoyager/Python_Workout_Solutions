# DomirScire

def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line

if __name__ == "__main__":
    print(get_final_line('./'))
