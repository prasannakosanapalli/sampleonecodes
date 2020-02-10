import json
import requests
import datetime
from jira import JIRA
credentials={"serviceAccount" : "farid.roshan@altimetrik.com", "serviceAccountToken" : "cA1AvOAgGdMaccejfgwy8919"}
jiraURL= "https://altimetrik.atlassian.net"
a= requests.get(jiraURL, credentials)
url = "/rest/api/3/project"
headers = {"Accept": "application/json"}
response = requests.request("GET",jiraURL+url,headers=headers)
rep = json.loads(response.text)
list = []
id_numbers=[]
for obj in rep:
    list.append(obj["name"])
    id_numbers.append(obj["id"])
    searhing= jiraURL+"/rest/api/3/search"
    headers = {"Accept": "application/json"}
for i in list:
    print(i)
    query = " 'jql': 'project = {}' ".format(i)
    resgets = requests.request("GET", searhing,headers=headers,params=query)
        
    #i = JIRA.search_issues(jql_str,'issuetype=story', maxResults=None)
    #print(resgets)
    #story=json.dumps(json.loads(resgets.text), sort_keys=True, indent=4, separators=(",", ": "))
print(story)
    
#print("total no of projects is :",len(list))
#print("list of projet_names is :" , list)

"""
searhing= jiraURL+"/rest/api/3/search"
headers = {"Accept": "application/json"}
query = {'jql': 'project = VCQI'}
resgets = requests.request("GET", searhing,headers=headers,params=query)
#i = JIRA.search_issues(jql_str,'issuetype=story', maxResults=None)
#print(resgets)
story=json.dumps(json.loads(resgets.text), sort_keys=True, indent=4, separators=(",", ": "))
with open("prasanna.json", "w") as p:
    p.write(story)
    p.close()

print("-------------------------------------------------")
issuetypes="/rest/api/3/issuetype"
headers = {"Accept": "application/json"}
response_issues = requests.request("GET",jiraURL+issuetypes,headers=headers)
issue_type = json.loads(response_issues.text)
issue_list = []
for obj in issue_type:
    issue_list.append(obj["name"])

print("total no of issues is :",len(issue_list))
print("list of issues is :" , issue_list)
print("-------------------------------------------------")

project_id="/rest/api/3/project/{projectIdOrKey}"
"""
"""
for obj in id_numbers:
    a=jiraURL+"/rest/api/3/project/{}".format(obj)
    headers = {"Accept": "application/json"}
    response_issues = requests.request("GET",a,headers=headers)
    b = json.loads(response_issues.text)

print("total no of issues is :",len(b))
print("list of issues is :" , b)
""" 

"""
print("----------------------------------------------------")
"""
"""
issing= "/rest/api/3/jql/match"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
payload = json.dumps( {"jqls": ["project = REPSUITE 2.0 ARCHIVE","issuetype = story"  ]} )
response = requests.request("POST",jiraURL+issing,data=payload,headers=headers)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
"""
"""
searhing= jiraURL+"/rest/api/3/search"
headers = {"Accept": "application/json"}
query = {'jql': 'project = VCQI'}
resgets = requests.request("GET", searhing,headers=headers,params=query)
#i = JIRA.search_issues(jql_str,'issuetype=story', maxResults=None)
#print(resgets)
story=json.dumps(json.loads(resgets.text), sort_keys=True, indent=4, separators=(",", ": "))
with open("prasanna.json", "w") as p:
    p.write(story)
    p.close()
    
#print(store)
    






