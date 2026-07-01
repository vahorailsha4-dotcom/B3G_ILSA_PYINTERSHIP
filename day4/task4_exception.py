def read_file_safely(filename):
    try:
        with open(filename,"r") as file:
            return file.read()
    except FileNotFoundError:
        return "File Not available"
print(read_file_safely("test.py"))