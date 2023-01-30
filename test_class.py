from pathlib import Path

class Config:
    def __init__(self):
        self.file_ops = None
        self.format_type = None
        self.root = None
        self.folder_dict = dict()

    def config(self):
        print("Instructions: Enter the digits 1 or 2 in the following sets of command")
        while True:
            try:
                file_operation = int(input("Create (1) or Delete (2) a file/folder?\n"))
                file_type = int(input("Create a File (1) or Folder (2):\n"))
                root_path = int(input("Select Drive: C (1) or D (2)\n"))
                break
            except ValueError:
                print("You did not enter a number.")

        return file_operation, file_type, root_path

    def checkConfig(self, file_operation, file_type, root_path):
        self.file_ops = 'CREATE' if file_operation == 1 else 'DELETE'
        self.format_type = 'FILE' if file_type == 1 else 'FOLDER'
        self.root = r'C:\\' if root_path == 1 else r'D:\\'

class showDirectory(Config):
    def __init__(self):
        super().__init__()

    def print_directory(self):
        count = 0
        for folder in Path(self.root).iterdir():
            if folder.is_dir():
                count += 1
                self.folder_dict[count] = str(folder)

        print(f"List of Folders in {self.root}")
        if not self.folder_dict:
            print("No current Folders inside")
        else:
            for (index, folder) in self.folder_dict.items():
                print(f"[{index}]: {folder}")

class FileOperations(Config):
    def __init__(self):
        super().__init__()


    def create(self):
        pass

    def delete(self):
        pass








def main():
    while True:
        directory.print_directory()
        target_path = input(f"\nEnter 'y' to create your {format} at {root}\nOr Select a Folder to create at (Enter the target number)\n")
        result = validateInput(path)
        # skips if result == True (let user carry on choosing directory)
        if not result:
            flow = response()
            if flow == 'q':
                break

if __name__ == "__main__":
    configuration = Config()
    file_operation, file_type, root_path = configuration.config()
    configuration.checkConfig(file_operation, file_type, root_path)
    directory = showDirectory()
    main()





#t = Config()
#file_operation, file_type, root_path = t.config()
#t.checkConfig(file_operation, file_type, root_path)
#print(t.format_type)