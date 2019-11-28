import os

## 파일 크기 반환
def getFileSize(fileName, directory):

    fileSize = os.path.getsize(directory+"/"+fileName)
    return str(fileSize)

## 파일 내용 반환
def getFileData(fileName, directory):
    #with open(directory + "\\" + fileName, "rb") as f:
    with open(directory + "/" + fileName, "rb") as f:
        data = bytearray(f.read())

        return data
