import json
import requests
import query_model

class LibgenAPI(query_model.IDownloadSiteAPI):
    _name = "Library Genesis"
    _link = "http://gen.lib.rus.ec/json.php?"

    def queryRecent(self, limit):
        requestURL = self._link + "fields=ID,Author,Title,Year,Language&timefirst=2014-05-01&mode=last"
        response = requests.get(requestURL)

        _data = response.text
        for result in json.loads(_data):
            self._results.append(result)

        return response
