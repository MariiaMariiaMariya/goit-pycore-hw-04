# path = "/Users/Mariia/Documents/Developer/repositories/goit-pycore-hw-04/salerys.txt"
path = "salerys.txt"

def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, "r") as f:
           for el in f:
                name, salary = el.strip().split(",")
                total += int(salary)
                count += 1

        if count > 0:
            average = total / count 
        else:
            print("no salarys")

    except FileNotFoundError:
        return "❌ Ошибка. Не удалось найти файл"

    
    return total, average
 
total, average =  total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")