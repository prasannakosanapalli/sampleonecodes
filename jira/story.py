from jira import JIRA

users = ["user1", "user2"] #Add a list of users
credentials={"serviceAccount" : "farid.roshan@altimetrik.com", "serviceAccountToken" : "cA1AvOAgGdMaccejfgwy8919"}
jiraURL= "https://altimetrik.atlassian.net"
a= requests.get(jiraURL, credentials)
print ("User \tStory Points")
"""
sum_incompl = 0
for element in JIRA.incompleted_issues(board_id, sprint_id): #gets Ticket ID
    issue = JIRA.issue(element.key)
    estimated_storrypoints = issue.fields.customfield_10663  # SP estimated for this ticket
    sum_incompl = sum_incompl + estimated_storrypoints

#Completed
sum_compl = JIRA.completedIssuesEstimateSum(board_id, sprint_id) 

#Print all
print("Sum Incompleted Issues: ",sum_incompl)
print("Sum Completed Issues ", sum_compl)
"""
block_size = 100
block_num = 0
while True:
    start_idx = block_num*block_size
    issues = JIRA.search_issues(jql, start_idx, block_size)
    if len(issues) == 0:
            # Retrieve issues until there are no more to come
        break
    block_num += 1
    for issue in issues:
        log.info('%s: %s' % (issue.key, issue.fields.summary))