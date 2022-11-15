import os

def load_scr():
    all_files = os.listdir(".")
    scripts = []
    for file in all_files:
        if file.endswith(".crowsh"):
            scripts.append(file)
    return scripts

def exec_all(scripts):
    for script in scripts:
        with open(script, "r") as s:
            text = s.read()
            os.system(text)

def crow_plugin():
    exec_all(load_scr())
    return ["echo Executed!"] * 3