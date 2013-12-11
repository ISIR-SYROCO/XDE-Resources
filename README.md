XDE-Resources
=============

Robot URDF/DAE pack and a python module that stores their paths.


Install:
--------

3 installations are possible:

develop
~~~~~~~

It creates a symbolic link of the src folder, for development purpose:

	python setup.py develop


python installation
~~~~~~~~~~~~~~~~~~~

The package is installed as a python package:

	python setup.py install [--user]


cmake installation
~~~~~~~~~~~~~~~~~~

Files are separated.
The python files are installed as a python package, but the collada and urdf
files are installed in the share folder of the install_path:

	mkdir _build
	cd _build
	cmake [-DCMAKE_INSTALL_PREFIX=install_path] ..
	make install


Examples:
---------
See `test/main.py`
