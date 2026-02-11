path = "/Users/Mariia/Documents/Developer/repositories/goit-pycore-hw-04/cats.txt"

def get_cats_info(path):
    animals = []

    with open(path, "r") as file:
        for line in file:
            cat = {}
            id, name, age = line.strip().split(",")
            cat["id"] = id
            cat["name"] = name
            cat["age"] = age
            animals.append(cat)   
        return animals
    
res = get_cats_info(path)
print(*res, sep="\n")