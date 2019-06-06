# Zendesk Mobile Ticket Viewer
This program can be used to used to view list of all the tickets and display a particular ticket in detail (given access to Zendesk API). The program is coded in python3 and webpages are rendered using flask api.

# Startup configurations and running instructions

1. Get a copy of this Repository by any preferable method.
2. Make sure you have python 3.X.X and python -pip install.
3. cd in to the root folder and run following command to install dependencies.
```
$ pip install -r requirements.txt
```
4. Then cd in to the app folder and run the following command
```
$ python main.py
```
5. While the flask app is running in the background navigate to following URL from your browser.
```
http://localhost:5000/index/
```

### To run tests.
1. cd in to the app folder and run the following command.
```
$ python unit_tests.py
```

# Code description
### responsibilities of python modules are described below
1. main.py : This module is responsible for delivering data to flask front end and rendering web pages

2. ticket.py : This module is the python ticket object which is throughout the application

3. tickets_factory.py : This module is responsible for creating above ticket object from the given inputs.

4. zendesk_api.py: This module is responsible for handling connections to zendesk API. 
