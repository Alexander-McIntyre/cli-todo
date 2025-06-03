import argparse

def todo():
    print("\n📝 Welcome to the CLI Todo App!")
    print("💡 Use -h or --help to see available options.\n")

    parser = argparse.ArgumentParser(
        prog="cli-todo",
        description="📋 Add, delete, and list your todo items from the command line.",
        epilog="☕ Tip: Stay focused. One task at a time!"
    )

    parser.add_argument('-a', '--add', help="Add a new todo item")
    parser.add_argument('-d', '--delete', help="Delete a todo item by ID")
    parser.add_argument('-l', '--list', action='store_true', help="List all todo items")

    args = parser.parse_args()

    if args.add:
        print(f"[✅] Task to add: '{args.add}'")
    elif args.delete:
        print(f"[🗑️] Task to delete: ID or keyword '{args.delete}'")
    elif args.list:
        print("[📃] Listing all tasks...")
    else:
        print("[ℹ️] No command provided.")
        print("👉 Try one of the following:")
        print("   -a 'task'    to add a new todo")
        print("   -d 'id'      to delete a task")
        print("   -l           to list all tasks")
        print("   -h           for full help\n")

if __name__ == "__main__":
    todo()

