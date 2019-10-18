# Developer Instructions
## Local
1. Download the app at: [https://github.com/vikketii/tsoha](https://github.com/vikketii/tsoha)
2. You should use python virtual environment (like venv) for installing dependencies. All used dependencies can be found in file 'requirements.txt'.
3. After installing them with pip, you can start the website in port 5000 in localhost by running 'python run.py' in the main folder. If you now go to the page [localhost:5000/](localhost:5000/) you should see the program running.


## Heroku
1. First check if everything works in local environment.
2. Then install heroku-cli tool.
3. Create heroku page by running 'heroku create "application-name"'.
4. Then run 'heroku config:set HEROKU=1' and after that 'heroku addons:add heroku-postgresql:hobby-dev'. You should now have postgresql database up and running in heroku.
5. Add heroku as one of the remotes for git and after that simply push the git project to heroku.