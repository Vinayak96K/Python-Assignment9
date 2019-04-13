from re import *

def CheckOccurance(sFile,strToCheck):
    try:
        fd=open(sFile,'r')
        print("Frequency of TEXT[{}] in FILE[{}] is :{}".format(strToCheck,sFile,len(findall(strToCheck,fd.read()))))
    except IOError as eObj:
        if(eObj.errno==2):
            print("File does not exists!")
    finally:
        pass

def main():
    sFileName=str(input("Enter file name:"))
    strCheck=str(input("Enter string to check frequency:"))
    CheckOccurance(sFileName,strCheck)


if __name__ == "__main__":
    main()