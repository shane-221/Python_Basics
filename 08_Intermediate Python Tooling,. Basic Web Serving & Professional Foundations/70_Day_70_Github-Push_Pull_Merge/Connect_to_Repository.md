Remote Git Workflow

# What is a remote?
- A remote repository is hosted elsewhere (e.g., GitHub).
- You push your local commits to this remote to share or back up your work.

# Steps to connect and push to a remote

1. Add the remote repository:
git remote add origin <repository-URL>
# 'origin' is the name you give to the remote

2. Rename your current branch to 'main':
git branch -M main

3. Push your code and set upstream tracking:
git push -u origin main
# This uploads your commits and links your local 'main' to 'origin/main'

# Notes:
- 'main' is the default branch where primary commits are stored.
- After setting upstream, you can use 'git push' and 'git pull' without specifying origin/main.