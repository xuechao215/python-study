import os
import sys
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        sys.exit(1)

def dev():
    """Run the development server."""
    print("Starting development server...")
    run_command("uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")

def install():
    """Install dependencies."""
    print("Installing dependencies...")
    run_command("pip install -r requirements.txt")

def test():
    """Run tests."""
    print("Running tests...")
    # 这里只是占位，实际应该使用 pytest
    run_command("python -m unittest discover tests")

def help():
    """Show available commands."""
    print("Available commands:")
    print("  python manage.py install  - Install dependencies")
    print("  python manage.py dev      - Run development server")
    print("  python manage.py test     - Run tests")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    command = sys.argv[1]
    if command == "install":
        install()
    elif command == "dev":
        dev()
    elif command == "test":
        test()
    else:
        help()
