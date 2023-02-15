import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_project = response.json()

for project in my_project:
    print(f"project Name: {project['name']}\n project Url{project['web_url']}\n")






