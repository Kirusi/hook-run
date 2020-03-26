import json
import os
import subprocess
from argparse import ArgumentParser


def run():
    parser = ArgumentParser(
        usage="%(prog)s [CMD]",
        description="""
            Runs command from an existing python virtual environment. Script looks
            for a private configuration file in the current working directory
            hook-run.json. If such file is found, it's expected to follow  format:
            ```
            {
                "path": "/home/user/my_project/venv/bin"
            }
            ```
            Where `path` points to the virtual environment to be used.
            If file is not found, then no bootstrapping is performed.

            After bootstrapping is done, then specified command is executed.
        """,
    )

    args, cmd_args = parser.parse_known_args()

    if not cmd_args:
        parser.print_usage()
        exit(1)

    if cmd_args and cmd_args[0] == "--":
        cmd_args.pop(0)
    if len(cmd_args) == 0:
        parser.print_usage()
        exit(1)

    config = {}
    fname = "hook-run.json"
    if os.path.isfile(fname):
        with open(fname) as json_file:
            config = json.load(json_file)
    if config and config.get("path"):
        if "PATH" in os.environ:
            os.environ["PATH"] = config["path"] + os.pathsep + os.environ["PATH"]
        else:
            os.environ["PATH"] = config["path"]

    subprocess.run(cmd_args, shell=False, check=True)


if __name__ == "__main__":
    run()
