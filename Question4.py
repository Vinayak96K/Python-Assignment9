from re import *

def CompareFiles(sFile1,sFile2):
    try:
        fd1=open(sFile1,'r')
        fd2=open(sFile2,'r')
        if(fd1.read()==fd2.read()):
            print("Both files have same data!")
        else:
            print("Both files does not have same data!")
    except IOError as eObj:
        if(eObj.errno==2):
            print(eObj.strerror)
    finally:
        pass

def main():
    strFileName1=str(input("Enter file name1:"))
    strFileName2=str(input("Enter file name2:"))
    CompareFiles(strFileName1,strFileName2)


if __name__ == "__main__":
    main()