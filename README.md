# Sheets

#### 29 October 2019
#### By **Kironji Kevin**

## Description
Sheets is a command line tool that helps in entry of data in an excel sheet. 

### User Stories

A user will name the Excel sheet to write data to. The program will then ask for all the columns that will be used to store data. Sheets then loops over all the columns given as it requests for the user to write data to each iterated column. When all columns in the first loop are filled, Sheets loops over to the next loop which is essentially the second row, and the user gets to fill all the columns in the second row(loop). This automated process will go on as long as the user is content that the Excel sheet has been written to his/her satisfaction.


## Technologies Used
```
1. Python 3.6.8 for linux
2. Python 3.7.5 for windows
3. XlsxWriter
```
## Application Download(windows)
 [Sheets](#)

## Prerequisites 

For the Unix diehards, to access this application you will need:
```
1. Pip3
2. Python 3+
3. XlsxWriter
4. Pyfiglet
```
## Installation
```
1. Install python3+
   $ sudo apt install python3
2. Create a folder, name it what you want. Dive in
3. Install pip3  
   $ sudo apt install python3-pip 
4. Inside the folder create a virtual environment.
   $ pip3 install virtualenv
   $ virtualenv venv ( you can use any name rather than venv )
   $ source venv/bin/activate ( Activate the environment )
5. pip3 install -r requirements.txt
6. Download entry.py file from my repository and place it in your folder
7. Fire up the application 
   $ python entry.py
8. Exit program
   $ ctrl + c
9. Exit virtual environment
   $ deactivate
```
## Important!
When giving column titles, always seperate them with a space.

## Saving Location
Sheets saves the created excel file in Desktop.

## Future Plans
As of writing this readme, Sheets application only writes to an excel sheet. This means that you cannot read an already existing excel file. This limits the users ability to continue writing to an existing excel sheet. A user cannot complete populating a half done excel file with this program for it creates a new excel file on every launch. With that in mind, completing this functionality is underway.

## Known bugs
No known bugs as at the completion of the project.

## Support and contact details
Feel free to reach me at karonjekevin67@gmail.com

### License
The project is under the [MIT](https://github.com/Fahari/Sheets/blob/master/LICENSE) licence
Copyright (c) 2019 **Kironji Kevin**
