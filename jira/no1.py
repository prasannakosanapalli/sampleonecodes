# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:57:02 2019

@author: pkosanapalli
"""

import json
import datetime
from pprint import pprint
import Query

final_dict = {}
create_date = datetime.date.today().strftime("%I:%M%p on %B %d, %Y")
query = Query.JiraQuery('mongodb://localhost:27017/','jira_db')
profile_dict = query.get_schema_metadata('collector_config')
projects_dict = {}
new_dict = {}

def construct_jira_schema(list,project):
    new_dict = {}
    config_list = query.get_api_endpoint(list)

    if project != "":
        config_list = { "Component" : "/components", "Version" : "/versions", "IssueType" : "&expand=project.issuetypes"}

    for key in config_list:
        json_dict = {}
        if (key == 'IssueType'):
            config_list[key] = '/rest/api/2/issue/createmeta?projectKeys=' + str(project) + (config_list[key])
        elif (key == 'Component') or (key == 'Version'):
            config_list[key] = '/rest/api/2/project/' + str(project) + (config_list[key])

        object_list = query.generate_API_request(str(config_list[key]))
        result_list = query.query_data_parser(object_list,key)

        if (list == 'serverAPIDict') :
            result_list = query.query_data_parser(object_list,'serverInfo')
        if result_list != None:
            json_dict[key] = result_list
            json_dict = json.dumps(json_dict, default=lambda x:x.__dict__, sort_keys=True, indent=4)
            json_dict = json.loads(json_dict)
            new_dict.update(json_dict)

    final_dict[list] = new_dict
    return new_dict

final_dict['executionDetails'] = profile_dict
construct_jira_schema('serverAPIDict','')
construct_jira_schema('jiraAPIDict','')

query.import_document(final_dict)

project_list = query.get_project_metadata('')


for project in project_list:
    proj_dict = construct_jira_schema('appConfigAPIDict', project)
    if proj_dict:
        projects_dict[project] = proj_dict
        projects_dict.update(projects_dict)
query.update_document('appConfigAPIDict',projects_dict)