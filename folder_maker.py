import os 
def folder_make(folder_name):
    os.makedirs(folder_name)
def folder_delete(folder_name):
    os.removedirs(folder_name)
# fname= input("Enter folder: ")    
# dir = f"C:/testing/my python code/{fname}"
# folder_make(dir)
for i in range(1,5):
    dir = f"C:\python folders/{i}" 
    folder_make(dir)
    print(f"{i} folder created.")