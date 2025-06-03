import argparse
import os

TODO_FILE = "todo.txt"

def read_task():
	if not os.path.exists(TODO_FILE):
		if os.name == 'posix':
			os.system('touch todo.txt')
		return print('File does not exist created todo.txt')
	with open(TODO_FILE, 'r') as file:
		lines = file.readlines()
	return print(lines)
	# checking if file exists, if not returns a print statement
	# if exists, read the file


def write_task(task):
	return
	# writes the added argument to the file at the end


def add_task(task):
	print(f"[✅] Task to add: '{task}'")
	# tasks = read_task()
	# append
	# write_task(task)
	# print feedback message


def delete_task(task_id):
	print(f"[🗑️] Task to delete: ID or keyword '{task_id}'")
	# reads the TODO_FILE
	# either match task and delete or match index


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

	parser = argparse.ArgumentParser(
		prog="cli-todo",
		description="📋 Add, delete, and list your todo items from the command line.",
		epilog="☕ Tip: Stay focused. One task at a time!",
	)

	subparsers = parser.add_subparsers(dest="command")
	parser.add_argument("-a", "--add", help="Add a new todo item")
	parser.add_argument("-d", "--delete", help="Delete a todo item by ID")

	# list command
	subparsers.add_parser("list", help="List all tasks")

	args = parser.parse_args()

	if args.add:
		add_task(args.add)
	elif args.delete:
		delete_task(args.delete)
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
