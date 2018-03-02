'''
@author: aonghus
'''
import requests

def parseFile(input):

    if input.startswith("http"):
        N, instructions = None, []
        uri = input
        r = requests.get(uri).text
        led_commands = r.splitlines()
        N = int(led_commands[0])
        for i in range(1, len(led_commands)):
                instructions.append(led_commands[i])
        return N, instructions
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return
