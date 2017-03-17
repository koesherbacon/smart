If the following error is encountered after `make` and/or `python setup.py install`, then **install python development** files. 
```fish
smart/ccache.c:25:20: fatal error: Python.h: No such file or directory
 #include <Python.h>
```

For apt (ubuntu, debian...):
```bash
sudo apt install python-dev  # for python2.x installs
sudo apt install python3-dev  # for python3.x installs
```
For fedora-rpm
```bash
sudo dnf install python-devel
```

For suse-rpm (Although, this might be slightly different since I do not use OpenSUSE myself. If the command below does not work, then use zypper to search for the python-devel files in question)
```bash
sudo zypper in python-devel
```

Good luck!
