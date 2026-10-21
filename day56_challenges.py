
# Day 56 — Mini Challenge: Folder Analyzer

folder = {
    "file1.txt": 120,
    "file2.txt": 250,
    "subfolder": {
        "file3.txt": 300,
        "file4.txt": 150,
        "file5.txt": 200
    }
}


def analyze(folder):
    total = 0

    for name, value in folder.items():
        if type(value) == dict:
            total += analyze(value)
        else:
            total += value

    return total


print(analyze(folder))  # 1020
