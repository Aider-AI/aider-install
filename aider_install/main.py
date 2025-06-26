import subprocess
import sys
import uv
import os

def install_aider():
    try:
        uv_bin = uv.find_uv_bin()
        subprocess.check_call([
            uv_bin, "tool", "install", "--force", "--python", "python3.12", "--with", "pip", "aider-chat@latest"
        ])
        subprocess.check_call([uv_bin, "tool", "update-shell"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install aider: {e}")
        sys.exit(1)


def main():
    install_aider()


if __name__ == "__main__":
    main()
