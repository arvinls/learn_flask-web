#!D:\flask\arvin\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'httpie==0.7.2','console_scripts','http'
__requires__ = 'httpie==0.7.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('httpie==0.7.2', 'console_scripts', 'http')()
    )
