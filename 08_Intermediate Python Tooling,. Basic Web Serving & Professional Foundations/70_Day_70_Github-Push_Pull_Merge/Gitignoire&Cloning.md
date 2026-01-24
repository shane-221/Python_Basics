Gitignore

- A .gitignore file tells Git which files and folders to ignore.
- Common things to ignore:
  - .venv (virtual environments)
  - Data files (e.g., .csv, .xlsx)
  - System files (e.g., .DS_Store)

Process:
1. Create a .gitignore file:
   New-Item -Path .gitignore -ItemType File

2. Add ignore patterns inside the file:
   # Ignore all text files
   *.txt

   # Ignore virtual environment
   .venv/

3. The .gitignore file should be placed at the top level of your project.