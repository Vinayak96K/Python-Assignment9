import sys

def CopyFileContents(sFile):
    try:
        fd=open(sFile,'r')
        fd2=open("Demo.txt",'w+a+x')
        fd2.write(fd.read())
    except IOError as eObj:
        if(eObj.errno==2):
            print(eObj.strerror)
    finally:
        pass

def main():
    if(len(sys.argv)>1):
        CopyFileContents(str(sys.argv[1]))

if __name__ == "__main__":
    main()