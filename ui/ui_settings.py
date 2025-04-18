import tomllib


def get_project_version():
    pyproject_path = "./pyproject.toml"
    with open(pyproject_path, "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["tool"]["poetry"]["version"]


version = [get_project_version(), "Settings compatible update", []]
run_directly = "true"
debug = "false"
log = "false"
loop_interval_seconds = 30
