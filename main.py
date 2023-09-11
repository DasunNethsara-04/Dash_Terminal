import os
import subprocess
import platform


class DashTerminal:
    """This is a terminal simulator application to understand how a terminal works. All the commands based on Linux terminal commands."""

    def __init__(self) -> None:
        # Initialize the current directory to the root directory
        self.current_dir: str = "/"
        self.running: bool = False
        self.os_name: str = platform.system()

    def run(self) -> None:
        # check the os name and clear the terminal
        if self.os_name == "Windows":
            os.system("cls")
        elif self.os_name == "Linux":
            os.system("clear")
        elif self.os_name == "Darwin":
            os.system("clear")
        elif self.os_name == "Java":
            os.system("clear")
        elif self.os_name == "FreeBSD":
            os.system("clear")

        # Run the terminal
        self.running = True
        print("Welcome to Dash Terminal!")
        while self.running:
            user_input: str = input(f"{self.current_dir}$ ")  # Get user input
            self.process_input(user_input)  # Process user input

    def process_input(self, user_input: str) -> None:
        # Process the user input
        try:
            if user_input == "exit":
                # Exit the terminal
                self.running = False
            elif user_input == "pwd":
                # Print the current directory
                print(self.current_dir)

            elif user_input == "help":
                # Print the help
                print("Commands:")
                print("\texit - Exit the terminal")
                print("\tpwd - Print the current directory")
                print("\tclear - Clear the terminal")
                print("\tls - List the files in the current directory")
                print("\topen - Open the current directory")
                print("\tcd [foler_name/path] - Change the current directory")
                print("\tmkdir [folder_name] - Create a new directory")
                print("\ttouch [file_name] - Create a new file")
                print("\trm [file_name] - Remove a file")
                print("\trmdir [folder_name] - Remove a directory")

            elif user_input == "version":
                # Print the version
                print("Dash Terminal v0.1.0")

            elif user_input == "author":
                # Print the author
                print("Dash Terminal was created by Dasun Nethsara")

            elif user_input == "whoami":
                # Print the current user
                print(f"Current user: {os.getlogin()}")

            elif user_input == "os":
                # Print the current OS
                print(f"Current OS: {self.os_name} {platform.version()}")

            elif user_input == "about":
                # Print the about
                print("Dash Terminal is a terminal simulator created by Dasun Nethsara")
                print("It is written in Python and it is open source")
                print(
                    "You can find the source code here: https://github.com/DasunNethsara-04/Dash_Terminal"
                )

            elif user_input == "clear":
                # Clear the terminal
                if self.os_name == "Windows":
                    os.system("cls")
                elif self.os_name == "Linux":
                    os.system("clear")
                elif self.os_name == "Darwin":
                    os.system("clear")
                elif self.os_name == "Java":
                    os.system("clear")
                elif self.os_name == "FreeBSD":
                    os.system("clear")

            elif user_input == "ls":
                # List the files in the current directory
                self.list_dir()

            elif user_input == "open":
                # Open the current directory
                if self.os_name == "Windows":
                    subprocess.run(["explorer", os.path.realpath(self.current_dir)])
                else:
                    subprocess.run(["open", os.path.realpath(self.current_dir)])

            elif user_input.startswith("cd"):
                # Change the current directory
                self.change_dir(user_input[3:])

            elif user_input.startswith("mkdir"):
                # Create a new directory
                os.mkdir(os.path.join(self.current_dir, user_input[6:]))

            elif user_input.startswith("touch"):
                # Create a new file
                f = open(os.path.join(self.current_dir, user_input[6:]), "w+")
                f.close()

            elif user_input.startswith("rm"):
                # Remove a file
                os.remove(os.path.join(self.current_dir, user_input[3:]))

            elif user_input.startswith("rmdir"):
                # Remove a directory
                os.rmdir(os.path.join(self.current_dir, user_input[6:]))

            else:
                if user_input != "":
                    # Command not found
                    print(f"DASH: {user_input}: command not found")
                else:
                    pass

        except Exception as e:
            # Print the error
            print(e)

    def list_dir(self) -> None:
        """List the files in the current directory"""
        for file in os.listdir(self.current_dir):
            print(file)

    def change_dir(self, new_dir: str) -> None:
        """Change the current directory"""
        if new_dir.startswith("/"):
            self.current_dir = new_dir
        else:
            self.current_dir = os.path.join(self.current_dir, new_dir)


if __name__ == "__main__":
    # Run the terminal
    os_simulator = DashTerminal()
    os_simulator.run()
