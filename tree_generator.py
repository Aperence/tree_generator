import os

directory = "."

def generate_tree(path, prefix="|"):
    dirs = []
    files = []
    for filename in os.listdir(path):
        if filename[0] == "." or filename[0] == "_":
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
        dirname = os.path.basename(dir)
        print(prefix + "---" + dirname)
        generate_tree(dir, prefix + "     |")
        print(prefix)

    for file in files:
        filename = os.path.basename(file)
        print(prefix + "---" + filename)


generate_tree(directory)
        