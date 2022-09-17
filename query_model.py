class ResultEntry:
    _data = {}

    def __init__(self, data):
        self._data = data

    def getName():
        pass
    def getSize():
        pass
    def getDownloadLinks():
        pass
    def getDescription():
        pass
    def getIdentifier():
        pass
    #Returns a dictionary of the entire result entry
    def getData():
        pass
    def __str__(self):
        return json.dumps(self._data)

class IDownloadSiteAPI:
    _name = ""
    _link = ""
    _results = []

    def queryTest(self):
        return requests.get(self._link)

    def queryRecent(self, limit):
        pass

    def querySearch(self, query):
        pass

    def getName(self):
        return self._name

    def getResults(self):
        return self._results

    def getURL(self):
        return self._link
