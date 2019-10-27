import subprocess
import sys


def install_prerequisite_packages():
    """
    Installs the third-party packages pytube and nltk using pip.
    This method must be invoked upon starting up the application.
    Text file 'prerequisites.txt' must be present in the directory.
    """
    file = open('prerequisites.txt')
    packages = file.read().splitlines()
    for package in packages:
        subprocess.call([sys.executable, "-m", "pip", "install", package])
    file.close()

