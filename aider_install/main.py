import subprocess
import sys
import uv
import os

def install_aider():
    try:
        subprocess.check_call(
            f"{uv.find_uv_bin()} tool install --python python3.12 aider-chat@latest",
            shell=True
        )
        subprocess.check_call("uv tool update-shell", shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install aider: {e}")
        sys.exit(1)


def main():
    install_aider()


if __name__ == "__main__":
    main()
