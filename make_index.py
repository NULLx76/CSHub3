#!/usr/bin/env python3
import os

if __name__ == '__main__':
    for subdir, dirs, files in os.walk("./content/"):
        with open(subdir + "/_index.md", "w") as f:
           f.seek(0)
           f.write("+++\n")
           f.write("title = \"" + subdir.split("/")[-1] + "\"\n")
           f.write("+++\n")
           f.truncate()