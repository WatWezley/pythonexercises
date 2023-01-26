import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1 / "sample_folder"
folder_a.mkdir(exist_ok=True)

file_paths = [
    folder_a / "private.img",
    folder_a / "lyric.txt",
    folder_a / "bible.txt",
    folder_a / "inside.csv"
]
for path in file_paths:
    path.touch()

print()
print(path1)
print(list(folder_a.iterdir()), end="")

print()
for file in folder_a.iterdir():
    print(file.name)

print()
for file in path1.iterdir():
    print(file.name)


print()
for file in folder_a.glob("*.img"):
    print(file.name)




print()
for file in path1.glob("**/*.img"):
    print(file.name)


print()
for file in path1.rglob("*.txt"):
    print(file.name)



path1 = pathlib.Path.cwd()
folder_a = path1 / "another_sample"
folder_a.mkdir(exist_ok=True)


source = path1 / "sample_folder"/"private.img"
print(source)
destination = path1 / "another_sample"/"private.img"
print(destination)
source.replace(destination)
