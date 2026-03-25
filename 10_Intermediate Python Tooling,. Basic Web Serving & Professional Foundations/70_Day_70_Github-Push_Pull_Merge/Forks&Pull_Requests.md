# Forking and Pull Requests

## Forking vs Cloning
- Forking creates your own copy of someone else's repository on GitHub.
- The forked repo lives under your GitHub account.
- Cloning creates a local copy of a repository on your machine.
- To fork a repo, click the "Fork" button on GitHub.

## Workflow After Forking
1. Fork the original repository on GitHub.
2. Clone your fork to your local machine:
   git clone <your-fork-url>

3. Make changes locally, then push them back to your fork:
   git add .
   git commit -m "Your message"
   git push

## Contributing Back to the Original Repository
- The original author can see who forked their project and what changes were made.
- To propose your changes, create a Pull Request (PR):
  - Go to your fork on GitHub.
  - Click "New Pull Request".
  - GitHub will show the differences between your fork and the original repo.
  - Add a comment explaining your changes.
  - Click "Create Pull Request".

## What Happens Next
- The pull request appears for the original author.
- They can review the changes, comment, request updates, or approve them.
- Once approved, they can merge the pull request into the main/master branch.