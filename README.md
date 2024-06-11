# Project name: 360 Manager
# this code is writter for 360 manager test automation task
# By: Narendra Singh

## About this code:
 This code is written using page obhect model. Below are the folder structure and useage of each folders 
 1. driver\test_base.py - Has BaseTest that contain all common function/method written (click, sendkey etc). this is created for code reusability
 2. pages - This folder contains object definition and method for each page ( login, customer, logout etc.)
 3. reports - html report generate after eacg test execution if html report command as listed below use for test execution
 4. testdata - folder contains testdata.json file for test data 
 5. tests - contains all test cases written for login, customer page.
 6. Utility - folder contain utility.py file that has listed below utility functions
    - common function to get the value from UI and update it in testdata.json file
    - generate customdata function to generate new customer and s3folder name each time code run so no need to update the value in json file.
 7. Conftest.py - conftest file that includes all fixtures, test confuration, and plugins shared across multiple files
 8. reuirements.txt - listed all dependency required to run this code.

## test coverage
This test cover 
- Login funtionality - Valid and invalid case
- create new user - Verify validation message shows up when rquired data is not entered, create a new customer, store login and pw info to json data file. The code generates name and s3 folder value automatically each time it runs.
- Log out and log back in with new customer account.
 

## pre-requsit 
- chrome/firefox browser should install on the machine.


## Installation
- unzipe the file in local machine
- open "360manager" folder in any code editor ( For Ex: visual studio code)
- Open Terminal window (if using VS code)
- activate the virtual enviroment by 'venvTest\Scripts\activate'
- install all dependecy listed in requirments.text file using pip install -r requirements.txt
- once install code is ready to run

## commands to run this code
 Run any of the below command 
 - pytest ( run the code in defeault chrome brower)
 - pytest --browser "chrome" --html=reports/report.html --self-contained-html  ( to run in chrom browser and generate html report)
 - pytest --browser "firefox" --html=reports/report.html --self-contained-html ( to run in firefox browser and generate html report)

## view result
if run wth html command then report.html file will be generated in \360manager\reports foldeer


