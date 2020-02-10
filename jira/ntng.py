# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:04:21 2019

@author: pkosanapalli
"""

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
    query = " 'jql': 'project = {}' ".format(i)
    resgets = requests.request("GET", searhing,headers=headers,params=query)
    print(resgets)    
    #i = JIRA.search_issues(jql_str,'issuetype=story', maxResults=None)
    #print(resgets)
    story=json.dumps(json.loads(resgets.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(story)
