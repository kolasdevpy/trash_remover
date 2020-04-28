# Smart remover
Smart remover - educational homework.
This python script create trash folder in home directory.

- autocreates trash directory and log file
- remove object => moves object in the trash directory
- recovery object from the trash => moves object from the trash to the past directory
- delete object from the trash => removes a link to an object
- clear all objects in the trash => removes trash directory and log file
- show information about operations => shows all log file in the trash
- show status the trash directory => recursively shows all objects in the trash
_____

# Created by
- Creaty by Artyom Kolas
- Minsk, Belarus, 2020

# License
- MIT
- Free Software
_____

# Instull
- git clone https://github.com/kolasdevpy/trash_remover.git
- cd /homework-smart_rm
- python3 setup.py sdist
- cd /dist 
- (sudo) pip3 install trash_remover-'version'.tar.gz

# Uninstall:
- (sudo) pip3 uninstall trash_remover