import os

directory = "."

def generate_tree(path, prefix="|"):
    dirs = []
    files = []
    for filename in os.listdir(path):
        if filename[0] == ".":
            continue
        if path != ".":
            f = os.path.join(path, filename)
        else:
            f = filename

        if os.path.isfile(f):
            files.append(f)
        else:
            dirs.append(f)

    for dir in dirs:
        print(prefix + "---" + dir)
        generate_tree(dir, prefix + "     |")
        print(prefix)

    for file in files:
        pass
        print(prefix + "---" + file)


generate_tree(directory)
        