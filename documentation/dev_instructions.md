# Developer Instructions
## Local
You should use python virtual environment (like venv) for installing dependencies. All used dependencies can be found in file 'requirements.txt'. After installing them with pip, you can start the website in port 5000 in localhost by running 'python run.py' in the main folder. If you now go to the page [localhost:5000/](localhost:5000/) you should see the program running.

## Heroku
Running the program in Heroku is really simple. First check if everything works in local environment. Then install heroku-cli tool. Create heroku page by running 'heroku create "application-name"'. Then run 'heroku config:set HEROKU=1' and after that 'heroku addons:add heroku-postgresql:hobby-dev'. You should now have postgresql database up and running in heroku. Add heroku as one of the remotes for git and after that simply push the git project to heroku.
