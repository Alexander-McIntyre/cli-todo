# test_cli.py

import subprocess
import os

TODO_FILE = "todo.txt"

def run_cmd(command):
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )
    return result.stdout.strip()

def setup_module(module):
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

def teardown_module(module):
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

def test_add_task():
    output = run_cmd('python todo.py add "Write unit tests"')
    assert 'Write unit tests' in output

def test_list_tasks():
    run_cmd('python todo.py add "Buy milk"')
    output = run_cmd('python todo.py list')
    assert 'Buy milk' in output

def test_delete_task():
    run_cmd('python todo.py add "Clean room"')
    output = run_cmd('python todo.py delete 1')
    assert 'Clean room' in output

def test_delete_invalid():
    output = run_cmd('python todo.py delete 99')
    assert 'does not exist' in output

def test_help_message():
    output = run_cmd('python todo.py -h')
    assert 'usage:' in output
    assert 'add' in output
    assert 'delete' in output
    assert 'list' in output

