import os

## 파일 크기 반환
def getFileSize(fileName):
    #fileSize = os.path.getsize(directory+"\\"+fileName)
    fileSize = os.path.getsize(fileName)
    return str(fileSize)

## 파일 내용 반환
def getFileData(fileName):
    #with open(directory + "\\" + fileName, "rb") as f:
    with open(fileName, "rb") as f:
        data = bytearray(f.read())


    return data