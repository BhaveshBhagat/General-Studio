# General-Studio
It is a web application with functionalities like file uploading, downloading and viewing.
Note:- In the Oleic_assign.py file, Only above functionalities are implemented. 

# Prerequisite:-
Following technologies need to be installed already before runnng the API :- Python, Flask, Sqlite3, werkzeug 
And all the given files are in a same folder before running and UPLOAD_FOLDER varibale set to the path where you want to store files in server.  

# Technology used:
Python Framework → Flask is used to develop API.
Database → sqlite3 used to manage DataBase
Front-end → Used HTML to interact with user request.

# Following pages are developed for front-end:
● Upload page - On this page users can upload files (zip, xlsx, xls, csv) along with their details.

○ Upload Page has following Form Fields
■ Project name
■ Organization name
■ Song metadata (xls)
■ Songe file (.zip)
■ Video metadata (xls)
■ Video file (.zip)
■ Image metadata (xls)
■ Image file (zip)

● View Uploads - On this page users can view their uploaded file can also download from this page. Showing upload details as table with download button for each file

○ View Page has following Form Fields
■ Project name
■ Organization name

# How to execute-
1. Simply run the Oleic_assign.py file in python shell and after running the file, you will get local environment url in python shell.
2. Copy the url and paste in the brower to launch the API.
3. Now you can upload, download and simply view the files.
