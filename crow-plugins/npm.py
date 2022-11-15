import json

def crow_plugin():
    package_json = None
    with open("package.json", "rb") as f:
        package_json = json.load(f)
    
    run_cmd = f'node {package_json["main"]}'
    test_cmd = package_json["scripts"]["test"]

    return ["NONE", run_cmd, test_cmd]