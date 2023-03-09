Group 28. Cmd war card game.
==========================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Group 28. Cmd war card game.

Software Requirement
--------------------------
This is the software you need to work with the development environment (For windows).



### Choco
This is how you install choco packet manager. This is a packet manager for windows.

Read more on [Install the Windows packet manager Chocolatey](https://chocolatey.org/install).

```
# In the windows powerShell (make sure you have administrative privilege)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Check if installed correctly
choco
```

### Make
This is how you install GNU make. This is to run game, test, documentation and UML diagrams simpler.

Read more on [Install GNU make](https://community.chocolatey.org/packages/make).

```
# In the windows powerShell (make sure you have administrative privilege)
choco install make

# Check if installed correctly
make --version
```

### Dot
This is how you install Graphviz (dot command).

Read more on [Graphviz project](https://graphviz.org/).

```
# In the windows powerShell (make sure you have administrative privilege)
choco install graphviz

# Check if installed correctly
dot -V
```






Get going
--------------------------

This is how you can work with the development environment. 

### make shure PYTHONPATH is set
Make shure that you have set the PYTHONPATH to the dir War-Card-Game

```
# In the root of the project
export PYTHONPATH=.
```

### Check version of Python

Check what version of Python you have. The program is developed on version 3.10.0.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```


### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.


### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```



### Run the code

The game can be started like this.

```
# In directory War-Card-Game
# Execute the main program
make start_game
```

All code is stored below the directory `war/`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode. Run validators in dir War-Card-Game.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

### Run the unittests

The testfiles are stored in the `test/` directory. Run test from dir War-Card-Game.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
start htmlcov/index.html
```


### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



### Run all the automated documentation and UML diagrams

You can generate all the documentation and UML diagrams directly.

```
# Generate documentation
make doc
```

You can open a web browser to inspect the documentation as a generated HTML report.

```
# Too see doc on war
start doc/pdoc/war/index.html

# Too see doc on test
start doc/pdoc/test/index.html
```


You can open an image viewer to inspect the UML diagrams as a generated .png files.

```
# Too see UML diagrams on war
start doc/pyreverse/war/classes.png
start doc/pyreverse/war/packages.png

# Too see UML diagrams on test
start doc/pyreverse/test/classes.png
start doc/pyreverse/test/packages.png
```



### Run the automated documentation

The documentation is generated on both the war dir and test dir. The documents are generated in dir doc/pdoc.

```
# Generate documentation
make pdoc
```


### Run the automated UML diagrams

The UML diagrams is generated on both the war dir and test dir. The diagrams are generated in dir doc/pyreverse.

```
# Generate documentation
make pyreverse
```


### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Remove files generated for documentation and UML diagrams
make clean-doc

# Do also remove all you have installed
make clean-all
```



More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.
