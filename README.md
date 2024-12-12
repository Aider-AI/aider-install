# aider-install

A streamlined installer for the [aider AI coding assistant](https://aider.chat).

## Quickly install aider

```bash
python -m pip install aider-install
aider-install
```

## Features

- Sets up aider with all dependencies in an isolated environment
- Automatically installs Python 3.12 if not present
- Uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management
- Zero configuration needed
- Only installs 2 packages in the original python environment: uv and aider-install.
No other dependencies pollute your python environment.

## Requirements

- macOS, Linux, or Windows
- Python 3.8+ (Python 3.12 will be installed if needed)

## How it works

1. Running `python -m pip install aider-install` installs:
  - The very minimal `aider-install` package, which provides the `aider-install` command.
  - The uv python package as its only dependency.
2. Running `aider-install` does this:

```bash
uv tool install --python python3.12 aider-chat
uv tool update-shell
```

## Documentation

- [Aider documentation](https://aider.chat)
- [uv package manager](https://docs.astral.sh/uv/)

## Support

For issues with the installer, please [open a GitHub issue](https://github.com/Aider-AI/aider/issues).
For aider usage questions, see the [aider documentation](https://aider.chat).
