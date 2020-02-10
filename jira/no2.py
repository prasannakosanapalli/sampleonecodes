# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:57:03 2019

@author: pkosanapalli
"""

import json
import datetime
import pprint
import Query

query = Query.JiraQuery('mongodb://localhost:27017/','jira_db')
project_list = query.get_project_metadata('5d6f692462ddc8281c867f1f')
priority_list = query.get_priority_metadata()
query.get_schema_metadata('collector_config')
user_list = query.get_userlist_metadata()
final_dict = {}
#pri_dict = {}

final_dict['Execution Date'] = datetime.date.today().strftime("%I:%M%p on %B %d, %Y")
final_dict['Type'] = 'Analytics_ResultSummary'

def construct_query(query_metadata):
    query.set_query_metadata(query_metadata)

def run_query(primary_list,secondary_list,query_name):
    pri_dict = {}
    for primary in primary_list:
        tmpList = []
        json_dict = {}

        for secondary in secondary_list:
            parameters = {'project' : primary, 'priority': secondary, 'assignee': secondary}
            query_data = query.parse_jira_query(**parameters)
            if query_data:
                return_list = query.execute_jira_query(query_data,secondary)
                if return_list:
                    json_dict[secondary] = return_list
            #        json_dict = json.dumps(json_dict, default=lambda x:x.__dict__, sort_keys=True, indent=4)
            #        json_dict = json.loads(json_dict)
        if json_dict:
            pri_dict[primary] = json_dict
    final_dict[query_name] = pri_dict


construct_query('number_By_Priority')
run_query(project_list,priority_list,'number_by_priority')

construct_query('number_Not_Closed_CreateDate_StartOfYear')
run_query(project_list,priority_list,'not_closed_createddate_beginofyear')

construct_query('number_Not_Updated_In_Month_CreateDate_StartOfYear')
run_query(project_list, priority_list,'not_updated_in_month')

#construct_query('number_Not_Closed_By_User')
#run_query(project_list,user_list,'not_closed_by_user')

#final_dict['test'] = tmp_dict
query.import_document(final_dict)