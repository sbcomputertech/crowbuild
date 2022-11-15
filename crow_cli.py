from sys import argv
import os
import crowlib

def cmd_init():
    print("Scaffolding crow project in:", os.getcwd())
    name = input("Project name :> ")
    author = input("Author :> ")
    crowlib.scaffold(name, author)

def cmd_build():
    crowlib.run("build")
def cmd_run():
    crowlib.run("run")
def cmd_test():
    crowlib.run("test")

if __name__ == "__main__":
    prog_args = argv[1:]
    if len(prog_args) < 1:
        print("Error: no command specified. Use 'crow help' to see all commands")
    elif prog_args[0] in ["h", "help"]:
        print("TODO: Help page")
    elif prog_args[0] in ["i", "init", "c", "create"]:
        cmd_init()
    elif prog_args[0] in ["b", "build"]:
        cmd_build()
    elif prog_args[0] in ["r", "run"]:
        cmd_run()
    elif prog_args[0] in ["t", "test"]:
        cmd_test()
