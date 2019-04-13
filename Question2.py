from sys import *

def readFile(sFile):
    try:
        fd=open(sFile,'r')
        print("-----------------------Reading from file-----------------------")
        print(fd.read())
        print('-------------------------Read complete-------------------------')
    except IOError as eObj:
        if(eObj.errno==2):
            print(eObj.strerror)
    finally:
        pass

def main():
    sFileName=str(input("Enter file name:"))
    readFile(sFileName)


if __name__ == "__main__":
    main()