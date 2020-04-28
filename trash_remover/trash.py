#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-

from . import smart_rm
import sys



def main():

    #  The start with checking for the existence of the "my_trash" directory and "log_file.txt"
    smart_rm.check_for_trash_dir()
    try:
        if   sys.argv[1] == 'rm':                                 #       trash rm
            print(smart_rm.remove())
        elif sys.argv[1] == 'dl':                                 #       trash dl
            print(smart_rm.del_from_trash())
        elif sys.argv[1] == 'clr':                                #       trash clr
            print(smart_rm.clear())
        elif sys.argv[1] == 'log':                                #       trash log
            print(smart_rm.show_log())
        elif sys.argv[1] == 'show':                               #       trash show
            print(smart_rm.show_all_obj_in_trash())
        elif sys.argv[1] == 'recov':                              #       trash recov
            print(smart_rm.recovery_object())
        elif sys.argv[1] == '-h' or sys.argv[1] == '-help':       #       trash  ,trash -h, trash -help
            smart_rm.helper_rm()
    except IndexError:
        smart_rm.helper_rm()


if __name__ == '__main__':
    main()


# EOF
