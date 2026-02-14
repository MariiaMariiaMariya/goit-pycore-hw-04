from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

path = Path(".")  

def print_tree(directory: Path, indent: str = ""):
    for item in directory.iterdir():
        if item.is_dir():
            print(indent + Fore.LIGHTBLUE_EX + f"📂 {item.name}")
            print_tree(item, indent + "   ")
        else:
            print(indent + Fore.LIGHTGREEN_EX + f"📄 {item.name}")

def main():
    if not path.exists():
        print(Fore.RED + "❌ Путь не существует")
        return

    if not path.is_dir():
        print(Fore.RED + "❌ Это не директория")
        return

    print(Fore.YELLOW + f"\nСтруктура директории: {path}\n")
    print_tree(path)

if __name__ == "__main__":
    main()
