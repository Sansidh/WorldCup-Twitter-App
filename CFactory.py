import CFileRead as fr

class CFactory():
    def __init__(self):
        FileHandlingObj = fr.CRead()
        FileHandlingObj.ReadFile("fifatest.csv")
        MovieData = self.FileHandlingObj.getFileData()

    def ReadFile(self):
        k = 0

    def getMovieData(self):
        k = 90