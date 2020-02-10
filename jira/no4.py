# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:57:04 2019

@author: pkosanapalli
"""

# -*- coding: ascii -*-
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
import json
import requests
import datetime
from jira import JIRA, JIRAError
from bson.objectid import ObjectId
create_date = datetime.date.today().strftime("%I:%M%p on %B %d, %Y")

class JiraQuery():

    def __init__(self,mongo_host, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db
        myclient = pymongo.MongoClient(self.mongo_host)
        db = myclient[self.mongo_db]
        self.jira_config_collection = db["jiraconfig"]

    def set_query_metadata(self,query_name):
        self.query_name = query_name
        jira_query_data = self.jira_config_collection.find_one({"Name": self.query_name})
        self.query_name = jira_query_data['Name']
        self.query_summary = jira_query_data['Summary']
        self.query_domain = jira_query_data['Domain']
        self.query_statement = jira_query_data['QueryStatement']
        self.query_parameters = jira_query_data['Parameters']

    def get_schema_metadata(self, schema):
        profile_dict = {}
        self.schema = schema
        self.collector_config_data = self.jira_config_collection.find_one({"Name": self.schema})
        self.username = self.collector_config_data['serviceAccount']
        self.user_token = self.collector_config_data['serviceAccountToken']
        self.address = self.collector_config_data['jiraURL']
        options = {'server': self.address}
        self.cookie = (self.username, self.user_token)
        self.jira = JIRA(options, basic_auth=self.cookie)

        profile_dict = {'Author' : 'collectJiraConfig.py', 'Application' : 'Jira', 'TargetHost' : self.address, 'CreationDate' : create_date}
        return profile_dict


    def get_api_endpoint(self, element):
        self.app_config_api_config = self.collector_config_data[element]
        return self.app_config_api_config

    def get_project_metadata(self,id):
        new_id = id
        if (id == ''): self.jira_config_data = self.jira_config_collection.find_one({"_id": ObjectId(self.object_id)})
        else : self.jira_config_data = self.jira_config_collection.find_one({"_id": ObjectId(new_id)})

        return_set = self.jira_config_data['jiraAPIDict']['Project']['elementData']
        return return_set

    def get_priority_metadata(self):
        self.priority_list = self.jira_config_data['jiraAPIDict']['Priority']['elementData']
        return self.priority_list

    def get_userlist_metadata(self):
        self.user_list = self.jira_config_data['jiraAPIDict']['Groups']
        return self.user_list

    def generate_API_request(self,endPoint):
        endPoint = self.address + endPoint
        response = requests.get(endPoint, auth=self.cookie).json()
        return response

    def query_data_parser(self,json_object, type):
        try:
            json_str = json.dumps(json_object)
            json_response = json.loads(json_str)
            iterator = 0
            itemList = []
            itemDict = {}
            if (type == 'IssueType'):
                for project in json_response['projects']:
                    for issuetype in project['issuetypes']:
                        element = (issuetype.get('name'))
                        itemList.append(element)
                        iterator += 1

            elif (type == 'serverInfo'):
                itemList = self.create_json_output('serverInfo',json_response)
                return itemList

            elif (type == 'Groups'):
                tmpList = []
                iterator = json_response['total']
                for groups in json_response['groups']:
                    element = (groups.get('name'))
                    itemList =  self.itimize_group_data(element)
                    group_users = self.create_json_output(type, itemList)
                    itemDict.update(group_users)
                return itemDict
            else:
                for item in json_response:
                    if (type == 'ProjectType') or (type == 'Project'): element = json_response[iterator]['key']
                    else: element = json_response[iterator]['name']
                    itemList.append(element)
                    iterator += 1

            if (iterator) != 0:
                iterator = str(iterator)
                data_dict = self.create_json_output(type,itemList)
                return data_dict
        except IndexError:
            return None

    def itimize_group_data(self,group_name):
        try:
            user_list = []
            user_dict = {}
            counter = 0
            print self.cookie
            response_data = requests.get(self.address + '/rest/api/2/group?groupname=' + str(group_name) + '&expand=users' , auth=self.cookie).json()
            json_str = json.dumps(response_data)
            json_response = json.loads(json_str)
            print json_response
            for user in json_response['users']['items']:
                user_name = (user.get('name'))
                user_list.append(user_name)
                counter =+ 1
            user_dict[group_name] = user_list
            return user_dict

        except requests.RequestException as err:
            print ("OOps: Something Else",err)

    def create_json_output(self,item_type,item_list):
        json_dict = {}
        json_list = []
        try:
            if item_list:
                for key in item_list:
                    if ((item_type == 'serverInfo') or (item_type == 'Groups')): json_dict[key] = item_list[key]
                    else:   json_list.append(key)
            if ((item_type != 'serverInfo') and (item_type != 'Groups')):
                json_dict['elementData'] = json_list
            return json_dict
        except IndexError:
            return None

    def import_document(self,document):
        self.object_id = self.jira_config_collection.insert(document, check_keys=False)
        print "object_id ====> \t"
        print self.object_id

    def update_document(self,key_name, document):
        self.jira_config_collection.update_one({'_id': self.object_id}, {"$set":{key_name : document}}, upsert=False)

    def parse_jira_query(self,**kwargs):
        query = eval(self.query_statement)
        return query

    def execute_jira_query(self,query,item):
        try:
            tmpDict = []
            self.result_set = self.jira.search_issues(query,maxResults=1000)
            if self.result_set:
                for item in self.result_set:
                    tmpDict.append(str(item))
        except JIRAError as e:
             print e.status_code, e.text
        return tmpDict