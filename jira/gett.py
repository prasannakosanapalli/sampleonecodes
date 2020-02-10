from jira import JIRA
import requests
import json

credentials={"serviceAccount" : "farid.roshan@altimetrik.com", "serviceAccountToken" : "cA1AvOAgGdMaccejfgwy8919"}
jiraURL= "https://altimetrik.atlassian.net"
a= requests.get(jiraURL, credentials)
projects_url = "/rest/api/3/project"

headers = {"Accept": "application/json"}
response = requests.request("GET",jiraURL+projects_url,headers=headers)
a=json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
project_list=[]

for obj in a:
    project_list.append({"id":obj['id'],"key":obj["key"],"name":obj["name"]})
    
    
print(project_list)
    