
try:
    file_name = open("path","w")
    file_name.write("Hello")
except IOError:
    print("Can not write in a closed file")
else:
    file_name.close()
    print("Successful")
