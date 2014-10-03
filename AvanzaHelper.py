import urllib.request
import json
import base64

class AvanzaHelper:
    BASE_URL = ""
    USERNAME = ""
    PASSWORD = ""

    def __init__(self, url):
        self.BASE_URL = url

    def RelativeUrl(self, suffix):
        return self.BASE_URL + suffix

    def AddCredentials(self, username, password):
        self.USERNAME = username
        self.PASSWORD = password

    def Get(self, url):
        req = urllib.request.Request(url, None, { "ctag" : "1122334455", "User-Agent" : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" })

        # ISO-8859-1
        if self.USERNAME != "" and self.PASSWORD != "":
            encoded = base64.b64encode((self.USERNAME + ":" + self.PASSWORD).encode("ISO-8859-1"))
            authHash = encoded.decode("utf-8")
            req.add_header("Authorization", "Basic " + authHash)

        res = urllib.request.urlopen(req)
        content = res.read().decode(res.headers.get_content_charset())

        return json.loads(content)