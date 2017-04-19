import shlex
import subprocess
import hdjLog

class SystemCommand(object):
    commandString=None
    commandList=None
    processList= None
    index=None
    stdin=None
    stdout=None

    def __init__(self, commandLine='ls -l | less'):
        self.commandString = commandLine
        self.commandparser()

    def execute(self):
        (self.stdin, self.stdout) = self.processList[self.index].communicate()[0]

    def commandparser(self):
        plist = self.commandString.split('|')
        index = 0
        for p in plist:
            p_parsed = shlex(p)
            if index == 0:
                self.processList.append(subprocess.Popen(p_parsed,stdout=subprocess.PIPE))
                index += 1
            else:
                self.processList.append(subprocess.Popen(p_parsed,stdin=self.processList[index - 1].stdout,stdout=subprocess.PIPE))
                index += 1

        self.index = index
