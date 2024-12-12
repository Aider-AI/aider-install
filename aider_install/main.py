import subprocess
import sys

def install_aider():
    try:
        subprocess.check_call([
            "uv", "tool", "install",
            "--python", "python3.12",
            "aider-chat",
        ])
        subprocess.check_call(["uv", "tool", "update-shell"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install aider: {e}")
        sys.exit(1)
