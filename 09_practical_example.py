# 09_practical_example.py
# 综合实战：简单的命令行待办事项应用 (CLI Todo App)
# 结合了：类、文件操作、JSON、异常处理、用户输入

import json
import os
import sys
from datetime import datetime

# 常量定义
TODO_FILE = "todos.json"

class TodoItem:
    def __init__(self, task, completed=False, created_at=None):
        self.task = task
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "task": self.task,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["task"], data["completed"], data["created_at"])

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.task} ({self.created_at})"

class TodoManager:
    def __init__(self, filename):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [TodoItem.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save_todos(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                data = [todo.to_dict() for todo in self.todos]
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving todos: {e}")

    def add_todo(self, task):
        new_todo = TodoItem(task)
        self.todos.append(new_todo)
        self.save_todos()
        print(f"Added: {task}")

    def list_todos(self):
        if not self.todos:
            print("No todos found.")
            return
        print("\n--- Todo List ---")
        for index, todo in enumerate(self.todos):
            print(f"{index + 1}. {todo}")
        print("-----------------")

    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
            self.save_todos()
            print(f"Completed: {self.todos[index].task}")
        else:
            print("Invalid todo index.")

    def delete_todo(self, index):
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            self.save_todos()
            print(f"Deleted: {removed.task}")
        else:
            print("Invalid todo index.")

def print_menu():
    print("\n=== Python Todo CLI ===")
    print("1. List Todos")
    print("2. Add Todo")
    print("3. Complete Todo")
    print("4. Delete Todo")
    print("5. Exit")

def main():
    manager = TodoManager(TODO_FILE)

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.list_todos()
        elif choice == "2":
            task = input("Enter task description: ")
            if task.strip():
                manager.add_todo(task)
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            manager.list_todos()
            try:
                index = int(input("Enter todo number to complete: ")) - 1
                manager.complete_todo(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            manager.list_todos()
            try:
                index = int(input("Enter todo number to delete: ")) - 1
                manager.delete_todo(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
