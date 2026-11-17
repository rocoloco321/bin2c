import argparse
import os

parser = argparse.ArgumentParser(description="Object to .c file by roco")
parser.add_argument('filename', help="Input file")
args = parser.parse_args()
filename, ext = os.path.splitext(args.filename)
with(
    open(filename+ext, "rb") as obj,
    open(filename+f"_{ext[1:]}.c", "w") as outC,
    open(filename+f"_{ext[1:]}.h", "w") as outH
):
    outH.write(f"#pragma once\n\nextern char {filename}_{ext[1:]}[];")
    outC.write("#include \"common.h\"\n")
    outC.write(f"#include \"{filename+f"_{ext[1:]}.h"}\"\n\n")
    outC.write(f"char {filename}_{ext[1:]}[] = ")
    outC.write("{\n")
    i = 0
    while byte := obj.read(1):
        outC.write(f"0x{byte[0]:X}, ")
        i+=1
        if i % 10 == 0:
            outC.write("\n")
    outC.write("\n};")
