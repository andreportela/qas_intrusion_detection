from os import listdir, remove
from os.path import isfile, join
from random import seed, randint
import time


seed(1)
folder = "medical_records/"
first_file_index = 0
seconds_to_sleep = 1

def start():
    global seconds_to_sleep
    while True:
        time.sleep(seconds_to_sleep)
        all_files = [file_name for file_name in listdir(folder) if isfile(join(folder, file_name))]
        number_of_files = len(all_files)
        if number_of_files == 0:
            seconds_to_sleep += 0.7
            print(f"folder is empty, trying to avoid that by increasing sleeping time to {seconds_to_sleep}")
            continue
        last_file_index = number_of_files - 1
        random_index = randint(first_file_index, last_file_index)
        file_marked_to_deletion = all_files[random_index]
        remove(join(folder, file_marked_to_deletion))
        print(f"deleted {file_marked_to_deletion}")
