from pathlib import Path

while True:
    try:
        file_type = int(input("Enter 1 to create a File or 2 for Folder:\n"))
        root_path = int(input("Select Drive: Enter 1 for C or 2 for D\n"))
        break
    except ValueError:
        print("You did not enter a number.")

def config():
   if file_type == 1 and root_path == 1:
       return "File", r'C:\\'
   elif file_type == 1 and root_path == 2:
       return "File", r'D:\\'
   elif file_type == 2 and root_path == 1:
       return "Folder", r'C:\\'
   elif file_type == 2 and root_path == 2:
       return "Folder", r'D:\\'

format, root = config()
# Create a dict to store all files and folders in current directory
folder_dict = dict()

def showDirectory(root):
    count = 0
    # Scans PATH if points to directory
    for folder in Path(root).iterdir():
        if folder.is_dir():
            count += 1
            folder_dict[count] = str(folder)
    print(f"List of Folders in {root}")
    if not folder_dict:
        print("No current Folders inside")
    else:
        for index, folder in folder_dict.items():
            print(f"[{index}]: {folder}")

def create(file_type_name, extension):
    # create folder if file_type = Folder
    if extension == '':
        folder = Path(root).joinpath(file_type_name + extension)
        folder.mkdir(exist_ok=True)
        return folder
    # create file if file_type = File
    file = Path(root).joinpath(file_type_name + extension)
    file.touch(exist_ok=True)
    return file

def validateInput(path):
    global root, folder_dict
    try:
        if path == 'y':
            if format:
                file_type_name = input(f"Enter the name of your {format}:\n")
                # ask for file extension if file_type = file
                if format == 'File':
                    extension = input(f"Enter your {format} type (example: '.pdf', '.txt'):\n")
                else:
                    extension = ''
                print(f"Creating your {format}.....")
                create(file_type_name, extension)
                print(f"The {format} {file_type_name+extension} has been successfully created at the path {root}!")
        # change PATH if 'path' variable in dictionary
        elif int(path) in folder_dict.keys():
            root = folder_dict[int(path)]
            # reset dictionary for next directory
            folder_dict.clear()
            # return a boolean flag to skip response()
            return True
    except ValueError:
        print("The number you entered is invalid")

def response():
    global format, root
    drives = {1: r'C:\\', 2: r'D:\\'}
    while True:
        reply = input("Enter 1 or 2 to create a File or Folder again or 'q' to exit\n")
        if reply == 'q':
            break
        elif reply.isdigit():
            format = 'File' if reply == '1' else 'Folder'
            path = int(input("Select Drive: 1 for C or 2 for D\n"))
            if path in drives:
                root = drives[path]
                break
            else:
                print("Invalid drive selected")
    return reply

def main():
    while True:
        showDirectory(root)
        path = input(f"\nEnter 'y' to create your {format} at {root}\nOr Select a Folder to create at (Enter the target number)\n")
        result = validateInput(path)
        # skips if result == True (let user carry on choosing directory)
        if not result:
            flow = response()
            if flow == 'q':
                break

if __name__ == "__main__":
    main()
