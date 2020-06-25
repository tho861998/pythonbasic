"""
import os
os.remove("demofile.txt")
"""
import os
if os.path.exists("demofile1.txt"):
    os.remove("demofile1.txt")
else:
    print("the file does not exist")