#WAP to demonastrate ingeration via github to fetch the details of users who have created pull requests on Kubernetes Github repo.

import requests

pull_requests_endpoint = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(pull_requests_endpoint)

output = response.json()

pr_creaters = {}

for i in range(len(output)):
    print(output[i]["user"]["login"])



# How to get all usernames with number of pull requests made by each user

for i in range(len(output)):
    name = output[i]["user"]["login"]
    print(output[i]["user"]["login"])
    if name in pr_creaters:
        pr_creaters[name]+=1
    else:
        pr_creaters[name]=1
print("username : prs")
for creater, count in pr_creaters.items():
    print(f"{creater} ==>> {count} PRs")

