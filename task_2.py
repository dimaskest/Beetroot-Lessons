class Boss:
    def __init__(self, id_: int, name: str, company: str) -> None:
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []        

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            if worker.company == self.company:
                self.workers.append(worker)
            else:
                print("We don't have a Boss of this company ")
        else:
            raise ValueError("Value is not an instance of a Worker class")

    def __repr__(self) -> str:
        return f"{self.name}"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss) -> None:
        self.id = id_
        self.name = name
        self.company = company
        self.boss = self.check_boss(boss)

    @staticmethod
    def check_boss(boss):
        if not isinstance(boss, Boss):
            raise ValueError("Value is not an instance of a Boss class")
        else:
            return boss

    def __repr__(self) -> str:
        return f"(Worker: '{self.name}', company: '{self.company}', boss: '{self.boss}')"


boss_1 = Boss(1, "Ivan", "Apple")
boss_2 = Boss(2, "Bryan", "Microsoft")
worker_1 = Worker(1, "Ben", "Apple", boss_1)
worker_2 = Worker(2, "John", "Microsoft", boss_2)
worker_3 = Worker(3, "Josh", "Microsoft", boss_2)

boss_1.add_worker(worker_1)
boss_2.add_worker(worker_2)
boss_2.add_worker(worker_3)
print(boss_1.workers)
print(boss_2.workers)