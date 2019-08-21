import os
import sys

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

out_file = open("at_script_result.txt", "w")

out_file.write("hello")

out_file.close()

exit(0)
