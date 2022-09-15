from multiprocessing import Value


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_dict = {i + 1: days[i] for i in range(len(days))}
reverse_dict = {value: key for key, value in days_dict.items()}

print(days_dict)
print(reverse_dict)