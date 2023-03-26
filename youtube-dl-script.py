#!/usr/bin/env python3
import sys
import subprocess

if len(sys.argv) < 2:
    print("Por favor, insira um link do YouTube.")
    sys.exit(1)

url = sys.argv[1]
command = f"youtube-dl -x --audio-format mp3 -o '%(title)s.%(ext)s' {url}"
subprocess.run(command, shell=True)
