# Branches and Merging

- Branches allow you to work on new features without affecting the main code.
- Only merge into 'main' when the work is stable and ready for deployment.

## Creating a new branch
git branch <branch-name>

## Switching to a branch
git checkout <branch-name>

## Checking which branch you're on
git branch
# The branch with the asterisk (*) is your current branch

## Merging a branch back into main
1. Switch to the main branch:
   git checkout main

2. Merge the feature branch into main:
   git merge <branch-name>

3. If Git opens a merge message editor:
   - Type :q! to quit without editing
   - Or write a message and save normally

# Notes:
- The old branch does NOT disappear after merging.
- You may need to push the updated main branch:
  git push -u origin main
  # Sets upstream tracking if not already set

- You can view branch history on GitHub:
  GitHub → Insights