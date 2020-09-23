from shutil import move
from os import listdir, path, makedirs, getlogin

DESKTOP_DIR = "C:\\Users\\%s\\Desktop\\" % (getlogin())
FOLDERS = {
    "Pictures": [".jpg", ".png", ".bmp", ".gif", ".jpeg"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".xls", ".ppt", ".csv", ".txt"], 
    "Projects": [],
}

while True:
    
    for folder in FOLDERS.keys():
    # gets through all folder names and repeat the loop for each directory in organizer
        f_dir = DESKTOP_DIR + folder
        if not path.isdir(f_dir):
        # if there's no current folder in loop on Desktop, create one
            makedirs(f_dir)

        for fileform in FOLDERS[folder]:
            moved_counter = 0
            if len(listdir(f_dir)) > 1: 
                for f in listdir(f_dir):   
                    if f.endswith(fileform) and not f.endswith(".ini"):
                        # if any file in current directory ends with any of its formats, move files to the right directory
                        # also it checks if file's format isn't .ini to avoid a problem with desktop.ini file 
                        move(f_dir + "\\" + f, "C:\\Users\\%s\\%s" % (getlogin(), folder))
                        moved_counter += 1 
                    else:
                        try:
                            move(f_dir + "\\" + f, DESKTOP_DIR + "\\")
                        except:
                            pass
                if moved_counter:
                    print(str(moved_counter) + "files moved!")                    
