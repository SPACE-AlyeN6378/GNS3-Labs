@echo off

REM Set your GitHub username and email
set GIT_USERNAME=SPACE-AlyeN6378
set GIT_EMAIL=alymooltazeem@gmail.com

REM Set your GitHub repository URL
set GITHUB_REPO_URL=https://github.com/SPACE-AlyeN6378/GNS3-Labs

REM Initialize Git repository
git init

REM Configure Git user
REM git config --global user.name "%GIT_USERNAME%"
REM git config --global user.email "%GIT_EMAIL%"

REM Add GitHub repository as remote origin
REM git remote add origin %GITHUB_REPO_URL%

REM Add all files to staging
git add .

REM Commit changes
set /p COMMIT_MESSAGE=Enter your commit message: 
git commit -m "%COMMIT_MESSAGE%"

REM Push to GitHub (master branch)
git push -u origin master

echo Upload to GitHub complete!
pause
