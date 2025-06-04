import argparse
import os

TODO_FILE = "todo.txt"

def read_task():
	if not os.path.exists(TODO_FILE):
		if os.name == 'posix':
			os.system('touch todo.txt')
		return print('File does not exist created todo.txt')
	with open(TODO_FILE, 'r') as file:
		return [line.strip() for line in file if line.strip()]
	# checking if file exists, if not returns a print statement
	# if exists, read the file


def write_task(tasks):
	with open("todo.txt", 'w') as file:
		for task in tasks:
			file.write(task + '\n')
	# writes the added argument to the file at the end


def add_task(task):
	tasks = read_task()
	tasks.append(task)
	write_task(tasks)
	print(f'added "{task}"')


def delete_task(index):
	tasks = read_task()
	if index < 1 or index > len(tasks):
		print(f'task "{index}" does not exist')
		return
	removed = tasks.pop(index-1)
	write_task(tasks)
	print(f'deleted "{removed}"')

def list_task():
	print("[📃] Listing all tasks...")
	tasks = read_task()
	if not tasks:
		print("no task")
	else:
		for i, task in enumerate(tasks, start=1):
			print(f"{i}. {task}")


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
		print("[ℹ️] No command provided.")
		print("👉 Try one of the following:")
		print("   -a 'task'    to add a new todo")
		print("   -d 'id'      to delete a task")
		print("   list         to list all tasks")
		print("   -h           for full help\n")


if __name__ == "__main__":
	main()
