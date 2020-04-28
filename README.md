# Smart remover
Smart remover - educational homework.
This python script create trash folder in home directory.

- autocreate the trash directory and log file and check with start every function
- remove an object (into trash folder) => move object in the trash directory
- recovery an object from the trash => move object from the trash to the past directory
- delete an object from the trash => remove a link to an object
- clear all objects in the trash => remove trash directory and log file
- show information about operations => show log file content
- show status the trash directory => recursively show all objects in the trash
_____

# Created by
- Created by Artyom Kolas
- Minsk, Belarus, 2020

# License
- MIT
- Free Software
_____

# Install:
- git clone https://github.com/kolasdevpy/trash_remover.git
- cd /homework-smart_rm
- python3 setup.py sdist
- cd /dist 
- (sudo) pip3 install trash_remover-'version'.tar.gz

# Uninstall:
- (sudo) pip3 uninstall trash_remover