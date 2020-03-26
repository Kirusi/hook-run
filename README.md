# hook-run

Python bootstrap to activate a virtual environment (venv, or conda) and run a command. Intended to be used with pre-commit pypi package. Inspired by [venv-run](https://github.com/guludo/venv-run)

Runs a command from an existing python virtual environment. Script looks
for a private configuration file in the current working directory
hook-run.json. If such file is found, it's expected to follow format:

```
{
    "path": "/home/user/my_project/venv/bin"
}
```

Where `path` points to the virtual environment to be used.
If configuration file is not found, then no bootstrapping is performed, but script proceeds with command execution

After bootstrapping is done, then specified command is executed.
