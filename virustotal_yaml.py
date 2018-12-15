# -----------------------------------
import os
import hashlib
import pprint as ppr
import yaml
import requests
# -----------------------------------
class Hash:
    def __init__(self):
        self.fileList = list()
        self.fileHashInfo = {"virustotal":{"resource":[], "api":virustotalApi}}

    # Instance method (1)
    def fileInfo(self):
        for f in os.listdir():
            self.fileList.append(os.path.abspath(f))

    # Instance method (2)
    def fileHash(self):
        for f in self.fileList:
            with open(f, 'rb') as fRead:
                data = fRead.read()
                self.fileHashInfo['virustotal']['resource']. \
                    append(hashlib.md5(data).hexdigest())
                fRead.close()
        ppr.pprint (self.fileHashInfo['virustotal']['resource'])

    # Instance method (3)
    def yamlFileCreate(self):
        with open("virustotalInformation.yml", "w") as f:
            yaml.dump(self.fileHashInfo, f, default_flow_style=False)
            f.close()
        print ("file create success")

class VT(Hash):
    def __init__(self):
        Hash.__init__(self)

    def virustotalRequest(self):
        apikey, hashinfo = self.SendApiKey()
        indx = 0
        for fileHash in hashinfo:
            self.params  = {'apikey': apikey[indx], 'resource': fileHash}
            self.headers = { "Accept-Encoding": "gzip, deflate",
                            "User-Agent" : "gzip,  My Python requests library example client or username"}
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                    params=self.params, headers=self.headers)
            json_response = response.json()['scans']
            for k, v in json_response.items():
                print (k, " : ", v['detected'])

            indx += 1

    def SendApiKey(self):
        with open("virustotalInformation.yml", "r") as f:
            contents  = yaml.load(f)
            myApiKey  = contents['virustotal']['api']        # list 형태
            hashValue = contents['virustotal']['resource']   # list 형태, file 해시
            print (hashValue)
            f.close()
        return myApiKey, hashValue

def main():
    node = VT()
    node.fileInfo()
    node.fileHash()
    node.yamlFileCreate()
    node.virustotalRequest()
if __name__ == "__main__":
    os.chdir("C:\\Users\\sleep\\Desktop\\target_dir")
    virustotalApi = ["408377a0 -- 생략",
                     "c2f5edb9 -- 생략",
                     "cda13808 -- 생략",
                     "5b8d384d -- 생략",
                     "8c70bb76 -- 생략",
                     "a7677e9d -- 생략",
                     "559615ce -- 생략",
                     "d91aec94 -- 생략",
                     "2d5d0f6b -- 생략",
                     "7e6f911e -- 생략"]
    main()