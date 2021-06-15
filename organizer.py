from shutil import move, Error
from os import listdir, getlogin

DESKTOP_DIR = "C:\\Users\\%s\\Desktop\\" % (getlogin())

def load_config():
    with open('config.txt') as f:
        lines = f.readlines()
        for line in lines:
            line.replace('\n','')
        PIC_FORMATS = lines[0].split('=')[1].split(',')
        DOC_FORMATS = lines[1].split('=')[1].split(',')

        return {'PIC_FORMATS': PIC_FORMATS, 'DOC_FORMATS': DOC_FORMATS}


def cleanup():
    config = load_config()
    moved_counter = 0
    unmoved_counter = 0

    for file in listdir(DESKTOP_DIR):
        for f in config['PIC_FORMATS'] + config['DOC_FORMATS']:
            if file.endswith(f):
                try:
                    if f in config['PIC_FORMATS']:
                        move(DESKTOP_DIR + file, "C:\\Users\\%s\\%s" % (getlogin(), "Pictures"))
                    elif f in config['DOC_FORMATS']:
                        move(DESKTOP_DIR + file, "C:\\Users\\%s\\%s" % (getlogin(), "Documents"))
                    moved_counter += 1
                    break
                except Error:
                    unmoved_counter += 1

    if moved_counter:
        print(str(moved_counter) + " files moved!")
    if unmoved_counter:
        print(str(unmoved_counter) + " files not moved. Try changing filenames.")
    if not (moved_counter and unmoved_counter):
        print("There are no files to move.")


if __name__ == "__main__":
    cleanup()
