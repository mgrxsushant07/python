import os 
def folder_make(folder_name):
    os.makedirs(folder_name)
fname= input("Enter folder: ")    
dir = f"C:/testing/my python code/{fname}"
folder_make(dir)