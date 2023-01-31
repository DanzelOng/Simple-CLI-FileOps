from backend import Config, Input, ShowDir, FileOps

def main():
    while True:
        s.print_directory()
        path = i.askInput()
        filename, extension = i.executeInput(path)
        if filename == False and extension == False:
            continue
        else:
            if i.file_ops == 'CREATE':
                created = f.create(filename, extension)
                print(f"The {f.format} {filename+extension} was successfully created in {created}!")
            elif i.file_ops == 'DELETE':
                deleted = f.delete(filename, extension)
                print(f"The {f.format} {filename+extension} was successfully deleted in {deleted}!")
            result = i.response()
            if result == 'q':
                break

if __name__ == "__main__":
    s = ShowDir()
    i = Input()
    f = FileOps()
    main()