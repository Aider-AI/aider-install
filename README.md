# aider-install

A streamlined installer for the [Aider AI coding assistant](https://aider.chat).

## Quickly install aider

```bash
python -m pip install aider-install
aider-install
```

## Features

- Automatically installs Python 3.12 if not present
- Uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management
- Sets up Aider with all dependencies in an isolated environment
- Zero configuration needed

## Requirements

- macOS, Linux, or Windows
- Python 3.8+ (Python 3.12 will be installed if needed)

## How it Works

Installs `uv` as a dependency of the aider-install package and then runs:

```bash
uv tool install --python python3.12 aider-chat
uv tool update-shell
```

## Documentation

- [Aider Documentation](https://aider.chat)
- [uv Package Manager](https://docs.astral.sh/uv/)

## Support

For issues with the installer, please open a GitHub issue.
For aider usage questions, see the [aider documentation](https://aider.chat).
