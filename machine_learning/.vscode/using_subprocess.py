import subprocess


with open('information.txt', 'w+') as file:
    out = subprocess.call(["ls", "-lha"], stdout=file)
    file.seek(0)
    information = file.read()

print(information)    