from github import Github
import os
import base64

if not os.path.isfile("gh_token.txt"):
    token = input("pls type your Github token")
    with open("gh_token.txt", mode="w", encoding="utf-8") as f:
        f.write(token)

with open("gh_token.txt", mode="r", encoding="utf-8") as f:
        g = Github(f.read())


#リポジトリ名
reponames = []
for repo in g.get_user().get_repos(type='owner'):
    reponames.append(repo.name)
print(reponames)

#指定リポ README
# reponame = "kansai-gamer/bash"

# repo = g.get_repo(reponame)
# contents = repo.get_contents("README.md")
# content = base64.b64decode(contents.content)

# print(content.decode())

#フォルダ表示
repo = g.get_repo("kansai-gamer/bash")
contents = repo.get_contents("")
for content_file in contents:
    print(content_file.name)
