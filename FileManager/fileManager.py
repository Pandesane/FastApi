from pathlib import Path


class FileManager():

    def __init__(self,*, shopDir: str, baseDir: str = 'E:\\WebServers\\fastapi\\dataBase') -> None:
        self.fileLocation = baseDir + '\\' + shopDir
        self.path = Path(f'{self.fileLocation}')
        self.createDirIfNotExists()

    def createDirIfNotExists(self):
        if not (self.path.exists()):
            self.path.mkdir()

    def saveFile(self, filename: str, file: bytes):
        with open(f'NewFile.{self.getFileType(filename)}', 'w') as f:
            f.write(bytes)

    def getFileType(self, fileName: str):
        fileType = fileName.split('.')[-1]
        return fileType
