from shutil import move, Error
from platform import system
from getpass import getuser
from os import listdir
from os.path import expanduser

DESKTOP_DIR = ""

if system() == 'Windows':
    DESKTOP_DIR = "C:\\Users\\%s\\Desktop\\" % (getuser())
elif system() == 'Darwin':
    DESKTOP_DIR = "/Users/%s/Desktop" % (getuser())
elif system() == 'Linux':
    DESKTOP_DIR = expanduser("~") + "/Desktop"

def load_config():
    with open('config.txt') as f:
        lines = f.readlines()

        return {'PIC_FORMATS': lines[0].split('=')[1].split(','), 
                'DOC_FORMATS': lines[1].split('=')[1].split(','),
                'DEFAULT_PICTURES_LOCATION': lines[2].split('=')[1].replace('\n',''),
                'DEFAULT_DOCUMENTS_LOCATION': lines[3].split('=')[1].replace('\n',''),
                'CUSTOM_PICTURES_LOCATION': lines[4].split('=')[1].replace('\n',''),
                'CUSTOM_DOCUMENTS_LOCATION': lines[5].split('=')[1].replace('\n','')}


def cleanup():
    config = load_config()
    moved_counter = 0
    unmoved_counter = 0

    for file in listdir(DESKTOP_DIR):
        for f in config['PIC_FORMATS'] + config['DOC_FORMATS']:
            if file.endswith(f):
                try:
                    if f in config['PIC_FORMATS']:
                        if config['DEFAULT_PICTURES_LOCATION'] == 'True':
                            move(DESKTOP_DIR + file, "C:\\Users\\%s\\%s" % (getuser(), "Pictures"))
                        else:
                            move(DESKTOP_DIR + file, config['CUSTOM_PICTURES_LOCATION'])
                    elif f in config['DOC_FORMATS']:
                        if config['DEFAULT_DOCUMENTS_LOCATION'] == 'True':
                            move(DESKTOP_DIR + file, "C:\\Users\\%s\\%s" % (getuser(), "Documents"))
                        else:
                            move(DESKTOP_DIR + file, config['CUSTOM_DOCUMENTS_LOCATION'])
                    moved_counter += 1
                    break
                except Error:
                    unmoved_counter += 1

    if moved_counter:
        print(str(moved_counter) + " files moved!")
    if unmoved_counter:
        print(str(unmoved_counter) + " files not moved. Try changing filenames.")
    if not (moved_counter or unmoved_counter):
        print("There are no files to move.")


if __name__ == "__main__":
    cleanup()
