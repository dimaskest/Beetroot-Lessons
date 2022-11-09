class CManager:
    counter = 0
    
    def __init__(self, poem_file, mode) -> None:
        self.file = poem_file
        self.mode = mode

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter

    def __enter__(self):
        CManager.counter += 1
        self.opened_file = open(self.file, self.mode)
        return self.opened_file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"\nManager was used {self.counter} times")
        
        if isinstance(exc_val, AttributeError):
            self.opened_file.close()
            print("--------Exception data below--------")
            raise AttributeError
        return None

# with CManager("poem.txt", "r") as file:
#     print("Start of CManager\n")
#     poems = file.read()
#     print(f"Poems from file are: \n\n{poems}")