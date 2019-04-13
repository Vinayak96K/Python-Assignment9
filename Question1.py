from sys import *

def chkExists(sFile):
    try:
        fd=open(sFile,'r')
        print("File exists!")
    except IOError as eObj:
        if(eObj.errno==2):
            print("File does not exists!")
    finally:
        pass

def main():
    sFileName=str(input("Enter file name:"))
    chkExists(sFileName)


if __name__ == "__main__":
    main()