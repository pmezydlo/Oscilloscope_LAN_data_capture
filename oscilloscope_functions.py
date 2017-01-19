import pip
import sys

def command(tn, scpi):
    print "SCPI to be sent: " + scpi
    wait = 1
    response = ""
    while response != "1\n":
        tn.write("*OPC?\n")
        response = tn.read_until("\n", 1)
        print "response: " + response

    tn.write(scpi + "\n")
    print "sent SCPI: " + scpi
    response = tn.read_until("\n", wait)

    return response

