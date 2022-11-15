# crowbuild
### a lightweight build system written in python

### usage:
- clone the source code into a folder
- create a python venv (make sure it is called crow-env): `python -m venv crow-env`
- add the folder to your PATH (not strictly necessary, but is useful to do)
- run `crow init` to scaffold a project
- use `crow build/run/test` to build projects

### plugins
Plugims go in the `<crow root>/crow-plugins` folder
Each plugin must be registered in the plugins.txt file, in the format `plugin id:python file`
The python files must contain a `crow_plugin()` function, that takes 0 parameters and returns a list of 3 strings.
The first string is the build command, the second is the run command, and the third is the test command.
These commands can be loaded from files, like what the NPM module does with package.json
