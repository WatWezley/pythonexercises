import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1 / "my_folder"
folder_a.mkdir(exist_ok=True)
print("how are you")

#file_paths = [
    #folder_a / "private.img",
    #folder_a / "lyric.txt",
    #folder_a / "bible.txt",
    #folder_a / "inside.csv"

#for path in file_paths:
    #path.touch()