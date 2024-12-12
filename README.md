# aider-install

A streamlined installer for the [aider AI coding assistant](https://github.com/Aider-AI/aider-install).

## Quickly install aider

```bash
python -m pip install aider-install
aider-install
```

## Features

- Automatically installs Python 3.12 if not present
- Uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management
- Sets up aider with all dependencies in an isolated environment
- Zero configuration needed

## Requirements

- macOS, Linux, or Windows
- Python 3.8+ (Python 3.12 will be installed if needed)

## How it Works

1. The `python -m pip install aider-install` installs uv as a dependency.
2. Running `aider-install` does this:

```bash
uv tool install --python python3.12 aider-chat
uv tool update-shell
```

## Documentation

- [Aider documentation](https://aider.chat)
- [uv package manager](https://docs.astral.sh/uv/)

## Support

For issues with the installer, please open a GitHub issue.
For aider usage questions, see the [aider documentation](https://aider.chat).
