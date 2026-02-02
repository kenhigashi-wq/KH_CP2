import csv

try:
    with open("notes/sample.txt", "r") as file:
        content = []
        for line in file:
            content.append(line.strip())
    print(content)
except:
    print("File not found.")
else:
    for line in content:
        print(f"Hello {line}")


try:
    with open("notes/Class CSV sample - Sheet1.csv", mode = "r", newline = '') as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1],
                }
            )
except:
    print("File not found.")
else:
    for user in users:
        print(user)