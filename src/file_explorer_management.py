import keys_vars as keys_vars
from os import path, listdir

# RELIES ON keys_vars.current_directory
def get_files_in_directory():
    cur_dir = keys_vars.current_directory
    if path.exists(cur_dir):
        