# DomirScire
import time

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)

if __name__ == "__main__":
    for t in elapsed_since('abcd'):
        print(t)
        time.sleep(2)
