import subprocess

def run_command(command):
    # This is potentially unsafe as it allows arbitrary command execution
    subprocess.call(command, shell=True)

def main():
    user_input = input("Enter a command to run: ")
    run_command(user_input)

if __name__ == "__main__":
    main()
