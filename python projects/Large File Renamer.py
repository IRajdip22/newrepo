import os

path = input("Enter the path of the folder: ")

print(os.listdir(path))

def main():
    i = 1
    for filename in os.listdir(path):
       new_name = path + str(i) + ".jpg"
       old_name = path + filename
       os.rename(old_name, new_name)
       i+=1

main()