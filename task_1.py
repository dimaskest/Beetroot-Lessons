import threading


counter = 0
rounds = 100000


class Counter(threading.Thread):
    def run(self):
        global counter
        global rounds
        for _ in range(rounds):
            counter += 1

thread_1 = Counter()
thread_2 = Counter()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(counter)