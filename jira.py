import json
import urllib.request
from jira import jira


class jira_conn:
    def __init__(self,address,port,protocol,user,passwd):
        self.jac = jira('{}://{}:{}'.format(protocol,address,port),basic_auth=(user,passwd))
    
    def test_connection(self,address,port,protocol):
        try:
            http_address = '{}://{}:{}/rest/api/latest/serverInfo'.format(protocol,address,port)
            req = urllib.request.Request(http_address)

            r = urllib.request.urlopen(req).read()
            cont = json.loads(r.decode('utf-8'))
            return cont["version"] 
        except:
            return "NOK"


    def jira_create_ticket(self, jac,issue_dict):
        try:
            issues = jac.create_issues(field_list=issue_dict)
            return issues
        except:
            return "NOK"

