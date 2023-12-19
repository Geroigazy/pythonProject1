import os
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__} is {end_time - start_time:.6f} seconds")
        return result
    return wrapper


class CommandPrompt:

    def __init__(self):
        self.current_directory = os.getcwd()

    def show_prompt(self):
        print(f"{self.current_directory}> ", end="")

    @timing_decorator
    def list_directories(self):
        try:
            items = os.listdir(self.current_directory)

            print('Files in the current directory:')
            for item in items:
                print(item)

        except OSError as e:
            print(f"Error: {e}")

    @timing_decorator
    def change_directory(self, directory):
        try:
            if directory == "..":
                self.current_directory = os.path.abspath(os.path.join(self.current_directory, os.pardir))
            else:
                self.current_directory = os.path.join(self.current_directory, directory)

        except FileNotFoundError:
            print(f"Directory '{directory}' not founded.")
        except Exception as e:
            print(f"Error: {e}")

    @timing_decorator
    def create_file(self, file_name):
        try:
            os.mkdir(os.path.join(self.current_directory, file_name))
            print(f"Directory '{file_name}' created")

        except FileExistsError:
            print(f"Directory '{file_name}' already exists.")
        except Exception as e:
            print(f"Error: {e}")

    @timing_decorator
    def delete_file(self, file_name):
        try:
            os.rmdir(os.path.join(self.current_directory, file_name))
            print(f"Directory '{file_name}' deleted")

        except FileNotFoundError:
            print(f"Directory '{file_name}' not founded.")
        except OSError as e:
            print(f"Error: {e}")

    @timing_decorator
    def rename_file(self, old_name, new_name):
        try:
            os.rename(os.path.join(self.current_directory, old_name), os.path.join(self.current_directory, new_name))
            print(f"Directory '{old_name}' renamed to '{new_name}'")

        except FileNotFoundError:
            print(f"Directory '{old_name}' not founded.")
        except FileExistsError:
            print(f"Directory '{new_name}' already exists.")
        except Exception as e:
            print(f"Error: {e}")

    @timing_decorator
    def view_file(self, file_name):
        try:
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                content = file.read()
                print(content)

        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except IsADirectoryError:
            print(f"'{file_name}' - это директория, а не файл.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


def main():
    cmd = CommandPrompt()
    while True:
        cmd.show_prompt()
        user_input = input()

        if user_input.lower() == "exit":
            print('Exiting Command Prompt. Goodbye!')
            break
        elif user_input == 'ls':
            cmd.list_directories()
        elif user_input.startswith('cd '):
            cmd.change_directory(user_input.split()[1])
        elif user_input.startswith('mkdir '):
            cmd.create_file(user_input.split()[1])
        elif user_input.startswith('rename '):
            cmd.rename_file(user_input.split()[1], user_input.split()[2])
        elif user_input.startswith('del '):
            cmd.delete_file(user_input.split()[1])
        elif user_input.startswith('open '):
            cmd.view_file(user_input.split()[1])
        elif user_input == 'pwd':
            print(f'Current directory: {cmd.current_directory}')
        else:
            print(f"Invalid input. Please enter valid func.")


if __name__ == '__main__':
    main()
