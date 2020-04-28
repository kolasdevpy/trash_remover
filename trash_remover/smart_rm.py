#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-

import datetime
import glob
import os
import shutil
import sys




ACCESS_RIGHTS = 0o0777
TRASH_DIR = os.path.expanduser("~/Documents/my_trash")          # OR ~/.my_trash
LOG_FILE = f'{TRASH_DIR}/log_file.txt'                          # OR ~/.log_file.txt
EMERGENCY_RECOVERY_DIR = os.path.expanduser("~/Documents")

def helper_rm():
    print('trash rm - moving file or directory including subdirectories and files in the trash directory')
    print('trash dl - delete object from the trash directory forever')
    print('trash clr - delete the trash directory and the log_file.txt')
    print('trash log - shows log_file.txt content')
    print('trash show - shows all object in the trash')
    print('trash recov - recovery file or directory including subdirectories and files')
    print('trash,  trash -h,  trash -help  -  help function')

###  BEGIN  checking for the existence of the "my_trash" directory and "log_file.txt"  ####

def check_for_trash_dir():
    '''checking for the existence of the "my_trash" directory and "log_file.txt" 
    with start every function'''
    if os.path.exists(TRASH_DIR) and not os.path.exists(LOG_FILE):
        create_log_file(TRASH_DIR)
    elif os.path.exists(TRASH_DIR) and os.path.exists(LOG_FILE):
        pass
    else:
        mk_dir(TRASH_DIR)

def mk_dir(TRASH_DIR):
    '''making the trash directory'''
    os.mkdir(TRASH_DIR, ACCESS_RIGHTS)
    print (f'{TRASH_DIR}\nTrash Directory has been created.\n')
    create_log_file(TRASH_DIR)
    return TRASH_DIR

def create_log_file(TRASH_DIR):
    '''auto creating the log_file.txt'''
    with open(LOG_FILE, 'w') as f:
        f.write((TRASH_DIR) + chr(10)*2)

###  END   checking for the existence of the "my_trash" directory and "log_file.txt"  #####


def log_operation(path, size):
    '''logging operations in the log_file.txt'''
    with open(LOG_FILE, 'a') as f:
        now = datetime.datetime.now()
        now = now.replace(microsecond=0)
        log = f'{now} - {size} bytes - from - {path} - removed to -> {TRASH_DIR + "/" + os.path.split(path)[1]}\n'
        f.writelines(log)
        return f'{log}'

def get_the_total_size(obj):
    '''shows full size of object'''
    byte_sum = 0
    if os.path.isfile(obj):
        byte_sum = os.path.getsize(obj)
    else:
        for top, dirs, files in os.walk(f'{obj}', topdown=True):
            size = os.path.getsize(top)
            byte_sum += size
            for nm in files:
                if nm.startswith('.') or nm.startswith('log_file.txt'):
                    dirs
                    pass
                else:
                    f_name = os.path.join(top, nm)
                    size = os.path.getsize(f_name)
                    byte_sum += size
    return byte_sum

def check_size_error(obj, spase):
    '''check sizes of object and directory for operation for avoid overflow error'''
    size = get_the_total_size(obj)
    free_space = int(shutil.disk_usage(spase)[2]) - 100000000
    print(f'free_space = {free_space}')
    print(f'obj__size  = {size}')
    if size > free_space:
        return f'''  \nSORRY
                    \rOperation is not impossible
                    \robj__size > free_space
                    \r{size} > {free_space}'''
    else:
        pass


def remove():
    '''moving file or directory 
        including subdirectories and files 
        in the trash directory'''
    obj_remove = None
    while obj_remove != 'q':
        obj_remove = input('''
            \rPlease, enter the full path to the directory or file
            \rwhich you want to remove.
            \rOR enter "q" to exit\n\n''')
        if obj_remove == 'q':
            exit()
        elif obj_remove == TRASH_DIR:
            return f'Please, use clr for delete trash directory?'
        elif not os.path.exists(obj_remove):
            return f'File or directory not found.'
        else:
            check_size_error(obj_remove, TRASH_DIR)
            try:
                size = get_the_total_size(obj_remove)
                shutil.move(obj_remove, TRASH_DIR)
                log_operation(obj_remove, size)
                return f'Object has been removed to: \n{TRASH_DIR}'
            except FileNotFoundError :
                return f'''\nSORRY!
                            \rFile or directory not found.
                            \rPlease specify the path for the remove directory or file.'''
            except shutil.Error:
                size = get_the_total_size(obj_remove)
                new_name = str(obj_remove) + ' -another- ' + str(datetime.datetime.today())
                os.renames(obj_remove, new_name)
                shutil.move(new_name, TRASH_DIR)
                log_operation(new_name, size)
                return f'Object has been removed to: \n{TRASH_DIR}'

def del_from_trash():
    '''delete object from the trash directory forever'''
    obj_clr = None
    while obj_clr != 'q':
        show_all_obj_in_trash()
        obj_clr = input('''
            \rPlease, enter full path of the object
            \rwhich you want to remove once and for all.
            \rOR enter "q" to exit\n\n''')
        if obj_clr == 'q':
            break
        elif not os.path.exists(obj_clr):
            return f'File or directory not found.'
        else:
            try:
                if os.path.isdir(obj_clr):
                    os.chmod(obj_clr, 0o0777)
                    shutil.rmtree(obj_clr, ignore_errors=False, onerror=None)
                else:
                    os.remove(obj_clr, dir_fd=None)
            except FileNotFoundError:
                return f'''\nSORRY!
                    \rFile or directory not founded.
                    \rPlease specify the path for the remove directory or file.'''
                continue
            else:
                return f'''Object has been removed once and for all:
                        \r{obj_clr}'''

def clear():
    '''delete the trash directory and the log_file.txt'''
    shutil.rmtree(TRASH_DIR, ignore_errors=False, onerror=None)
    return f'{TRASH_DIR}\nHas been deleted'

def show_log():
    '''shows log_file.txt content'''
    with open(LOG_FILE, 'r') as f:
        for line in f:
            print(line)

def show_all_obj_in_trash():
    '''unites funktions show_all_dirs() and show_all_objects()'''
    show_all_dirs()
    show_all_objects()

def show_all_dirs():
    '''shows all main (root) directories in the trash'''
    print(f'\n---------- The trash has next main directories: ----------\n')
    tr_dr = glob.glob(TRASH_DIR + '/*')
    for dirs in tr_dr:
        if os.path.isfile(dirs):
            pass
        else:
            print(dirs)

def show_all_objects():
    '''shows all objects in the trash and in subdirectories'''
    print(f'\n--------------- All objects in the trash: ----------------\n')
    d = 'folder'
    f = 'file'
    b = ' bytes  -- path ->'
    for top, dirs, files in os.walk(f'{TRASH_DIR}'):
        print("{:6s} {:15d} {:8s}  {:10s}".format(d, get_the_total_size(top), b, top))
        for nm in files:
            if nm.startswith('.') or nm.startswith('log_file.txt'):
                dirs
                pass
            else:
                f_name = os.path.join(top, nm)
                size = os.path.getsize(f_name)
                print("{:6s} {:15d} {:8s}  {:10s}".format(f, size, b, f_name))

def not_found_dir(path):
    '''if directory for recreating has been deleted, 
    function recreating object in ~/user_name/Documents'''
    print(f'''Directory not found.
            \rObjeckt will be recreate in the:
            \r{EMERGENCY_RECOVERY_DIR}''')
    try:
        print(f'Object has been removed to: \n{EMERGENCY_RECOVERY_DIR}')
        shutil.move(path, EMERGENCY_RECOVERY_DIR)
    except (FileNotFoundError, shutil.Error):
        pass

def recovery_object():
    '''recovery file or directory including subdirectories and files'''
    path = None
    while path != 'q':
        show_all_obj_in_trash()
        path = input('''\nPlease, enter the full path to object
                        \rwhich you want to recovery.
                        \rOR enter "q" to exit\n\n''')
        if path == 'q':
            break
        elif not os.path.exists(path):
            print('''\nObject not found.
                    \rEnter path to object once again.\n''')
        elif path == TRASH_DIR:
            print('''\nYou can only recovery objects IN the trash.
                    \rBut not the whole trash.''')
        else:
            with open(f'{LOG_FILE}', 'r') as f:
                for line in f:
                    if path in line:
                        print(line)
                        old_path = line.split()[8]
                        old_path_directory = os.path.split(old_path)[0]
                        check_size_error(path, old_path_directory)
                        try:
                            if os.path.isdir(old_path_directory):
                                print(f'Object has been removed to: \n{old_path_directory}')
                                shutil.move(path, old_path_directory)
                                return 0
                            else:
                                print(f'''Directory not found.
                                        \rDirectory will be recovered in the {EMERGENCY_RECOVERY_DIR}''')
                                flag = input(f'''{old_path_directory} directory not found.\n
                                                \rcreate non-existent directories and save them there - enter '1'
                                                \rmove the directory to the {EMERGENCY_RECOVERY_DIR} - enter - '2'    
                                                \rOR enter "q" to exit\n''')
                                if flag == '1':
                                    print(f'Object has been removed to: \n{old_path_directory}')
                                    os.makedirs(old_path_directory, mode=0o777, exist_ok=False)
                                    shutil.move(path, old_path_directory)
                                    return 0
                                elif flag == '2':
                                    print(f'Object has been removed to: \n{EMERGENCY_RECOVERY_DIR}')
                                    shutil.move(path, EMERGENCY_RECOVERY_DIR)
                                    return 0
                                elif flag == 'q':
                                    break
                                else:
                                    print(f'Please specify your comand')
                        except (FileNotFoundError, shutil.Error):
                            pass
                else:
                    print('----------')
                    not_found_dir(path)

# EOF
