import pip
import sys

def command(tn, scpi):
    wait = 1
    response = ""
    while response != "1\n":
        tn.write("*OPC?\n")
        response = tn.read_until("\n", 1)

    tn.write(scpi + "\n")
    response = tn.read_until("\n", wait)

    return response

