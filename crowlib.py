import crow_meta
import crow_parse
import os, sys, importlib

def scaffold(project_name: str, project_author: str):
    template = ""
    with open(os.environ.get("crow_root") + "/crow-scaffold/build.crow", "r") as f:
        template = f.read()
    template = template.replace("@CROW_VERSION", crow_meta.CROW_VERSION)
    template = template.replace("@PROJECT_NAME", project_name)
    template = template.replace("@PROJECT_AUTHOR", project_author)

    use_plugin = input("Would you like to use a build plugin [yes: plugin name / no]? ")
    if use_plugin != "no":
        template = template.replace("@BUILD_COMMANDS", "use_plugin=" + use_plugin)
    else:
        build_command = input("Enter build command [command / NONE]: ")
        run_command = input("Enter run command [command / NONE]: ")
        test_command = input("Enter test command [command / NONE]: ")
        cmd_strings = [
            "build-cmd=" + build_command,
            "run-cmd=" + run_command,
            "test-cmd=" + test_command
        ]
        template = template.replace("@BUILD_COMMANDS", "\n".join(cmd_strings))

    with open("build.crow", "w") as f:
        f.write(template) 

def run(action: str):
    if action not in ["build", "run", "test"]:
        raise ValueError("Not a valid crow command action")
    p = crow_parse.CrowFile()

    if p.config.has_option("build", "use_plugin"):
        plugin = p.config.get("build", "use_plugin")
        plugin_module = ""
        with open(os.environ.get("crow_root") + "/crow-plugins/plugins.txt") as f:
            lines = f.readlines()
            for line in lines:
                split = line.split(":")
                if split[0] == plugin:
                    plugin_module = split[1]
        
        sys.path.append(os.environ.get("crow_root") + "/crow-plugins")
        mod = importlib.import_module(plugin_module.removesuffix(".py").removesuffix(".py\n"), __name__)
        cmds = mod.crow_plugin()
        
        print("Loaded module '", plugin_module.removesuffix(".py").removesuffix(".py\n"), "'.")
        cmd_map = {"build":0,"run":1,"test":2}
        cmd_index = cmd_map[action]

        if cmds[cmd_index] == "NONE":
            print(f"ERROR: No {action} command specified")
            return
        os.system(cmds[cmd_index])
        
        return

    if action == "build":
        cmd = p.config.get("build", "build-cmd")
        if cmd == "NONE":
            print("ERROR: No build command specified")
            return
        os.system(cmd)
    elif action == "run":
        cmd = p.config.get("build", "run-cmd")
        if cmd == "NONE":
            print("ERROR: No run command specified")
            return
        os.system(cmd)
    elif action == "test":
        cmd = p.config.get("build", "test-cmd")
        if cmd == "NONE":
            print("ERROR: No test command specified")
            return
        os.system(cmd)