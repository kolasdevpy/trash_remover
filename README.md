# Smart remover
Smart remover - educational homework.
This python script create trash folder in home directory.

- remove object (file or folder) => moves to the trash
- recovery object from the trash => moves from the trash to the past directory
- delete object from the trash => removes a link to an object
- clear all objects from the trash => removes trash directory
- show information about operations => recursively shows all objects in the trash
- show information about operations => shows all log file in the trash

# Created by
>  Creaty by Artyom Kolas
>  Minsk, Belarus, 2020

# License
MIT
Free Software
_____
# Instull
git clone https://github.com/kolasdevpy/homework-smart_rm.git
cd /homework-smart_rm
python3 setup.py sdist
cd /dist 
(sudo)  pip3 install trash_remover-'version'.tar.gz

# Uninstall:
(sudo) pip3 uninstall trash_remover