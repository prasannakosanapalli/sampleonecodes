# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:57:06 2019

@author: pkosanapalli
"""

{
    "_id" : ObjectId("5d23eff5a38ac325a4895592"),
    "Name" : "collector_config",
    "Type" : "Default_Collector_Config",
    "serviceAccount" : "farid.roshan@altimetrik.com",
    "serviceAccountToken" : "cA1AvOAgGdMaccejfgwy8919",
    "jiraURL" : "https://altimetrik.atlassian.net",
    "serverAPIDict" : {
        "serverInfo" : "/rest/api/2/serverInfo"
    },
    "jiraAPIDict" : {
        "Groups" : "/rest/api/2/groups/picker",
        "Priority" : "/rest/api/2/priority",
        "Field" : "/rest/api/2/field",
        "ProjectType" : "/rest/api/2/project/type",
        "Project" : "/rest/api/2/project",
        "Status" : "/rest/api/2/status"
    },
    "jiraAPIDictBackup" : {
        "Groups" : "/rest/api/2/groups/picker",
        "Field" : "/rest/api/2/field",
        "Workflow" : "/rest/api/2/workflow",
        "ProjectType" : "/rest/api/2/project/type",
        "Priority" : "/rest/api/2/priority",
        "Project" : "/rest/api/2/project",
        "Resolution" : "/rest/api/2/resolution",
        "Status" : "/rest/api/2/status"
    },
    "appConfigAPIDict" : {
        "Component" : "/components",
        "Version" : "/versions",
        "IssueType" : "&expand=project.issuetypes"
    }
}