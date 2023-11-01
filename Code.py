#!/usr/bin/env python3
import io
import os
import queue
import uuid


class Code:
    def __init__(self, outFile):
        self.outFile = outFile
        self.counter = 0
        self.vmFileName = None
        self.labelCounter = 0

    # DONE
    def close(self):
        self.outFile.close()

    # DONE
    def updateVmFileName(self, name):
        self.vmFileName = os.path.basename(name).split(".")[0]

    # DONE
    def commandsToFile(self, commands):
        for line in commands:
            self.outFile.write(f"{line}\n")

    # DONE
    def getUniqLabel(self):
        return self.vmFileName + str(self.labelCounter)

    # DONE
    def updateUniqLabel(self):
        self.labelCounter = self.labelCounter + 1

    # DONE
    def writeHead(self, command):
        self.counter = self.counter + 1
        return ";; " + command + " - " + str(self.counter)

    # DONE
    def writeInit(self, bootstrap, isDir):
        commands = []

        if bootstrap or isDir:
            commands.append(self.writeHead("init"))

        if bootstrap:
            commands.append("leaw $256,%A")
            commands.append("movw %A,%D")
            commands.append("leaw $SP,%A")
            commands.append("movw %D,(%A)")

        if isDir:
            commands.append("leaw $Main.main, %A")
            commands.append("jmp")
            commands.append("nop")

        if bootstrap or isDir:
            self.commandsToFile(commands)

    # TODO
    def writeLabel(self, label):
        commands = []
        commands.append(self.writeHead("label") + " " + label)

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeIf(self, label):
        commands.append(self.writeHead("if") + " " + label)
        commands = []

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeArithmetic(self, command):
        self.updateUniqLabel()
        if len(command) < 2:
            print("instrucão invalida {}".format(command))
        commands = []
        commands.append(self.writeHead(command))

        if command == "add":
            pass # TODO
        elif command == "sub":
            pass # TODO
        elif command == "or":
            pass # TODO
        elif command == "and":
            pass # TODO
        elif command == "not":
            pass # TODO
        elif command == "neg":
            pass # TODO
        elif command == "eq":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO
        elif command == "gt":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO
        elif command == "lt":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO

        self.commandsToFile(commands)

    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        elif segment == "local":
            # dica: usar o argumento index (push local 1)
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "this":
            pass # TODO
        elif segment == "that":
            pass # TODO
        elif segment == "temp":
            # dica: usar o argumento index (push temp 0)
            pass # TODO
        elif segment == "static":
            pass # TODO
        elif segment == "pointer":
            pass # TODO

        self.commandsToFile(commands)

    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":
            # dica: usar index para saber o valor da consante
            # push constant index
            pass # TODO
        elif segment == "local":
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "this":
            pass # TODO
        elif segment == "that":
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "static":
            pass # TODO
        elif segment == "temp":
            pass # TODO
        elif segment == "pointer":
            pass # TODO

        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        # TODO
        # ...

        self.commandsToFile(commands)
