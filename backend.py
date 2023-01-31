from pathlib import Path

class Config:

    file_ops = None
    format = None
    root = None
    folder_dict = dict()

    def config(self):
        while True:
            try:
                file_operation = int(input("Create (1) or Delete (2)?\n"))
                file_type = int(input("File (1) or Folder (2)?:\n"))
                root_path = int(input("C (1) or D (2) drive?\n"))
                break
            except ValueError:
                print("You did not enter a valid number.")

        Config.file_ops = 'CREATE' if file_operation == 1 else 'DELETE'
        Config.format = 'FILE' if file_type == 1 else 'FOLDER'
        Config.root = r'C:\\' if root_path == 1 else r'D:\\'

    @classmethod
    def changeRoot(cls, modif):
        Config.root = modif
        Config.folder_dict.clear()

class Input(Config):

    def askInput(self):
        target_path = None
        if self.file_ops == 'CREATE':
            target_path = input(f"\nEnter 'y' to create your {self.format} at {self.root}\nOr Select a Folder to create at (Enter the target number)\n")
        elif self.file_ops == 'DELETE':
            target_path = input(f"\nEnter 'y' to delete your {self.format} at {self.root}\nOr Select a Folder to delete at (Enter the target number)\n")
        return target_path

    def executeInput(self, path):
        filename = False
        extension = False
        try:
            if path == 'y':
                if self.file_ops == 'CREATE':
                    filename = input(f"Enter the name of your {self.format}:\n")
                    if self.format == 'FILE':
                        extension = input(f"Enter your {self.format} type (example: '.pdf', '.txt'):\n")
                    else:
                        extension = ''
                elif self.file_ops == 'DELETE':
                    filename = input(f"Enter the name of your {self.format} you wan to delete:\n")
                    if self.format == 'FILE':
                        extension = input(f"Enter the extension of the {self.format} (example: '.pdf', '.txt'):\n")
                    else:
                        extension = ''
            elif int(path) in self.folder_dict.keys():
                root = self.folder_dict[int(path)]
                Input.changeRoot(root)
        except ValueError:
            print("The number you entered is invalid")

        return filename, extension

    def response(self):
        while True:
            reply = input("Continue again? Enter to continue or press 'q' to exit.\n")
            if reply == 'q':
                break
            c.config()
            break
        return reply

class ShowDir(Config):

    def print_directory(self):
        count = 0
        for folder in Path(self.root).iterdir():
            if not self.file_ops == 'DELETE':
                if folder.is_dir():
                    count += 1
                    self.folder_dict[count] = str(folder)
            else:
                count += 1
                self.folder_dict[count] = str(folder)

        print(f"List of Folders in {self.root}")
        if not self.folder_dict:
            print("No current Folders inside")
        else:
            for (index, folder) in self.folder_dict.items():
                print(f"[{index}]: {folder}")

class FileOps(Config):

    def create(self, filename, extension):
        if extension == '':
            folder = Path(self.root).joinpath(filename+extension)
            folder.mkdir(exist_ok=True)
            return folder

        file = Path(self.root).joinpath(filename+extension)
        file.touch(exist_ok=True)
        return file

    def delete(self, filename, extension):
        if extension == '':
            folder = Path(self.root).joinpath(filename+extension)
            folder.rmdir()
            return folder

        file = Path(self.root).joinpath(filename+extension)
        file.unlink()
        return file

c = Config()
c.config()
