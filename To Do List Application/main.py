import pyfiglet
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print()
print(pyfiglet.figlet_format("Welcome TODO List Application", font="slant"))

task_list = []


def main_menu() -> None:
    print()
    print(f"{Fore.YELLOW}{Style.BRIGHT} 1 : Display Tasks")
    print(f"{Fore.YELLOW}{Style.BRIGHT} 2 : Add New Task")
    print(f"{Fore.YELLOW}{Style.BRIGHT} 3 : Complete Task")
    print(f"{Fore.YELLOW}{Style.BRIGHT} 4 : Delete Task")
    print(f"{Fore.YELLOW}{Style.BRIGHT} 5 : Exit Programme")
    print()


def add_task(task_name: str) -> None:
    task = (task_name, False)  # (task_name, completed_status)
    task_list.append(task)


def display_tasks() -> None:
    if not task_list:
        print(f"{Fore.RED}No tasks available.")
        return

    for number, (name, completed) in enumerate(task_list, start=1):
        status = f"{Fore.GREEN}✔ Completed" if completed else f"{Fore.RED}✘ Not Completed"
        print(f"{Fore.CYAN}{Style.BRIGHT}{number} : {name} [{status}]")


def complete_task(task_number: int) -> None:
    if 1 <= task_number <= len(task_list):
        name, _ = task_list[task_number - 1]
        task_list[task_number - 1] = (name, True)


def delete_task(task_number: int) -> None:
    if 1 <= task_number <= len(task_list):
        task_list.pop(task_number - 1)


while True:
    main_menu()
    choice = input("Enter Your Choice : ")
    print()

    if not choice.isdigit():
        print(f"{Fore.RED}Invalid input, please enter a number.")
        continue

    choice = int(choice)

    if choice == 1:
        display_tasks()

    elif choice == 2:
        task_name = input("Enter Task Name : ")
        add_task(task_name)

    elif choice == 3:
        if not task_list:
            print(f"{Fore.RED}No tasks to complete.")
            continue
        display_tasks()
        task_number = input("Enter Task Number : ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(task_list):
            complete_task(int(task_number))
        else:
            print(f"{Fore.RED}Invalid task number.")

    elif choice == 4:
        if not task_list:
            print(f"{Fore.RED}No tasks to delete.")
            continue
        display_tasks()
        task_number = input("Enter Task Number : ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(task_list):
            delete_task(int(task_number))
        else:
            print(f"{Fore.RED}Invalid task number.")

    elif choice == 5:
        print(f"{Fore.YELLOW}Exiting Programme... Goodbye!")
        break

    else:
        print(f"{Fore.RED}Invalid choice, please select between 1–5.")
