# Version Control (Git)

- Git is a version control system that tracks changes to code.
- Git Bash is the terminal program used to run Git commands.

# Installing Git
- Download Git for Windows from: https://git-scm.com
- Enable "Git Bash" during installation.
- You can open Git Bash directly or switch your terminal to Bash.

# Local Git Workflow

## 1. Initialise a repository
git init

## 2. Check file status
git status
# Red = untracked/modified
# Green = staged

## 3. Add files to the staging area
git add .
# or
git add <filename>

## 4. Commit staged changes
git commit -m "Describe what this commit does"

## 5. View differences from last commit
git diff <filename>

## 6. Revert a file to the last committed version
git checkout <filename>

## 7. View commit history
git log