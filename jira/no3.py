# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:57:04 2019

@author: pkosanapalli
"""

{
    "_id" : ObjectId("5d1df59ba38ac325a4895516"),
    "Author" : "froshan",
    "Type" : "Query",
    "Name" : "number_By_Priority",
    "Summary" : "list number of objects based on priority per project",
    "CreateDate" : "June 04 2019",
    "Domain" : "Priority",
    "QueryStatement" : "'project=\\\"' + '{project}'.format(**kwargs) + '\\\" AND priority=\\\"' +  '{priority}'.format(**kwargs) + '\\\"'",
    "Parameters" : {
        "project" : "{}.format(proj)",
        "priority" : "{}.format(priority)"
    }
}

/* 2 */
{
    "_id" : ObjectId("5d234aaaa38ac325a489555e"),
    "Author" : "froshan",
    "Type" : "Query",
    "Name" : "number_Not_Closed_CreateDate_StartOfYear",
    "Summary" : "list number of objects based on priority per project that are still not closed",
    "CreateDate" : "June 04 2019",
    "Domain" : "Priority",
    "QueryStatement" : "'project=\\\"' + '{project}'.format(**kwargs) + '\\\" AND priority=\\\"' +  '{priority}'.format(**kwargs) + '\\\"' + 'AND createdDate <= startOfYear() and status != \\\"Closed\\\"'",
    "Parameters" : {
        "project" : "{}.format(proj)",
        "priority" : "{}.format(priority)"
    }
}

/* 3 */
{
    "_id" : ObjectId("5d2357c9a38ac325a4895569"),
    "Author" : "froshan",
    "Type" : "Query",
    "Name" : "number_Not_Closed_By_User",
    "Summary" : "list number of objects by uer that are created at StartofYear and still not closed",
    "CreateDate" : "July 8 2019",
    "Domain" : "User",
    "QueryStatement" : "'project=\\\"' + '{project}'.format(**kwargs) + '\\\" AND assignee=\\\"' +  '{assignee}'.format(**kwargs) + '\\\"' + 'AND createdDate <= startOfYear() and status != \\\"Closed\\\"'",
    "Parameters" : {
        "project" : "{}.format(proj)",
        "priority" : "{}.format(priority)"
    }
}

/* 4 */
{
    "_id" : ObjectId("5d236475a38ac325a489557c"),
    "Author" : "froshan",
    "Type" : "Query",
    "Name" : "number_Not_Updated_In_Month_CreateDate_StartOfYear",
    "Summary" : "list number of objects based on priority per project that are still not closed",
    "CreateDate" : "June 04 2019",
    "Domain" : "Date",
    "QueryStatement" : "'project=\\\"' + '{project}'.format(**kwargs) + '\\\" AND priority=\\\"' +  '{priority}'.format(**kwargs) + '\\\"' + 'AND createdDate <= startOfYear() AND updatedDate <= startOfMonth() AND status != \\\"Closed\\\"'",
    "Parameters" : {
        "project" : "{}.format(proj)",
        "priority" : "{}.format(priority)"
    }
}