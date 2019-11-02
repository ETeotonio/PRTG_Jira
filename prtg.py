import json
import urllib.request

class prtg:
    def __init__(self,server,user, password, port,protocol):
        self.http_address = "{}://{}:{}/api/table.json?username={}&password={}".format(protocol, server,port,user,password).replace("\"","")


    def test_connection(self,address):
        try:
            http_address = '{}&content=sensors&columns=sensors'.format(address)
            req = urllib.request.Request(http_address)

            r = urllib.request.urlopen(req).read()
            cont = json.loads(r.decode('utf-8'))
            return cont["prtg-version"]
        except:
            return "NOK"
    
    def get_current_alerts(self,address,ack_status):
        try:
            http_address = '{}&content=sensors&columns=group,device,sensor,status,lastvalue,priority'.format(address)
            req = urllib.request.Request(http_address)

            r = urllib.request.urlopen(req).read()
            content = json.loads(r.decode('utf-8'))
            for sensor in content['sensors']:
                if(sensor['status']=='Down'):
                    print(sensor['device'],sensor['sensor'],sensor['status'],sensor['lastvalue'],sensor['priority'])
        except:
            print("Connection Failed")