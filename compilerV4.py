import os




asmfile = open("code.asm","a")
assembly = """.686p
.mmx
.xmm
option casemap :none
include \masm32\include\masm32rt.inc
include \masm32\include\kernel32.inc
include \masm32\include\masm32.inc
includelib \masm32\lib\kernal32.lib
includelib \masm32\lib\masm32.lib
.data
"""

file =open("code.txt","r").read()
code=file.split("\n")

external = ""
#combines
for search in code:
    search=search.split(" ")
    if search[0] == "combine":
        file=open(search[1],"r").read()+"\n"+file
        code=file.split("\n")

#Varibles and data

#assembly=assembly+".data\n"
data = {}
for command in code:
    command=command.split(" ")
    try: 
        if command[5] == "=":
            for i in range(4): command.remove("")
    except: pass
    try:
        if command[1] == "=":
            build = ""
            variblename = command[0]
            command.remove(command[0])
            command.remove(command[0])
            for word in command: build=build+" "+word
            data[variblename] = build[1:]
    except: pass


def checkint(x):
    intiger = False
    try: int(data[varible]) ; intiger=True
    except: pass
    return intiger

#writing data section
for varible in data:
    if data[varible][0] == '"':
        assembly=assembly+"    "+varible+" db "+data[varible]+", 0\n"
    elif data[varible][0] == "*":
        assembly=assembly+"    "+varible+" db "+data[varible][1:]+", 0\n"
    elif checkint(data[varible]):
        assembly=assembly+"    "+varible+" dword "+data[varible]+"\n"
    else:
        assembly=assembly+"    "+varible[1:]+" dword 10\n"





#commands
def assemblecode(code,arguments):
    asm = ""
    code=code.replace("    ","")
    code=code.split("\n")
    asm=asm+"    pop esi\n"
    argscopy = [x for x in arguments]
    if arguments[0] != "null":
        for i in range(len(arguments)):
            asm=asm+"    pop "+arguments.pop()+"\n"
    for command in code:
        if command == "": pass
        elif command[0] == "/":
            asm=asm+"    "+command[1:]+"\n"
        elif "=" not in command:
            if " " in command:
                args = command.split(" ")
                args.remove(args[0])
                for arg in args:
                    if arg in argscopy:
                        asm=asm+"    push "+arg+"\n"
                    elif arg[0] == ".":
                        asm=asm+"    push "+arg[1:]+"\n"
                    else:
                        asm=asm+"    push offset "+arg+"\n"
            asm=asm+"    call "+command.split(" ")[0]+"\n"
    asm=asm+"    push esi\n"
    return asm





assembly=assembly+".code\n"
funcs = file.split("#")
for lable in funcs:
    if "{" not in lable: pass
    else:
        funccode = lable.split("{")
        definition = funccode[0].replace(" ", "")
        name = definition.split("(")[0]
        args = definition.split("(")[1].split(")")[0].split(",")
        assembly=assembly+name+":\n"
        commands = funccode[1].split("}")[0][1:]
        assembly=assembly+assemblecode(commands,args)
        #assembly=assembly+"    invoke ExitProcess, 0\n"
        if name == "main": assembly=assembly+"end main\n"
        else: assembly=assembly+"    ret\n"


print(assembly)
#exit()
asmfile.write(assembly)
asmfile.close()
print("Assembling")
os.system("C:/masm32/bin/ml /c /Zd /coff code.asm")
print("Compiling")
os.system("C:/masm32/bin/link /SUBSYSTEM:CONSOLE code.obj")
os.system("del code.asm")
os.system("del code.obj")
