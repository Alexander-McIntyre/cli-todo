import argparse
import os

TODO_FILE = "todo.txt"


def file_exists():
    #Graceful error handling
    if not os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'w') as file:
                pass
            print("[🌱] A new todo list has created")
        except IOError as e:
            print(f"[❌] Couldn't create the todo list Error: {e}")
            sys.exit(1)


def read_tasks():
    file_exists()
    with open(TODO_FILE, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def write_task(tasks):
	#Helper function for both add and delete
	with open("todo.txt", 'w') as file:
		for task in tasks:
			file.write(task + '\n')


def add_task(task):
	tasks = read_tasks()
	tasks.append(task)
	write_task(tasks)
	print(f'added "{task}"')


def delete_task(index):
	tasks = read_tasks()
	if index < 1 or index > len(tasks):
		print(f'task "{index}" does not exist')
		return
	removed = tasks.pop(index-1)
	write_task(tasks)
	print(f'deleted "{removed}"')

def list_task():
	print("[📃] Listing all tasks...")
	tasks = read_tasks()
	if not tasks:
		print("no task")
	else:
		for index, task in enumerate(tasks, start=1):
			print(f"{index}. {task}")


def main():
	print("\n📝 Welcome to the CLI Todo App!")
	print("💡 Use -h or --help to see available options.\n")

	#parsers
	parser = argparse.ArgumentParser(
		prog="cli-todo",
		description="📋 Add, delete, and list your todo items from the command line.",
		epilog="☕ Tip: Stay focused. One task at a time!",
	)

	subparsers = parser.add_subparsers(dest="command")
	
	#add command
	parser_add = subparsers.add_parser("add", help="Adding a task to todo.txt")
	parser_add.add_argument('task', type=str, help="task description")

	#delete command
	parser_delete = subparsers.add_parser("delete", help="Adding a task to todo.txt")
	parser_delete.add_argument('index', type=int, help="task number to delete")

	# list command
	subparsers.add_parser("list", help="List all tasks")

	args = parser.parse_args()

	if args.command == "add":
		add_task(args.task)
	elif args.command == "delete":
		delete_task(args.index)
	elif args.command == "list":
		list_task()
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
