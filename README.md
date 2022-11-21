# formResponseAutomater
The python Script above is using Selenium Webdriver to automatically control the given google form and fill the required the responses.
It uses Pandas library to create and use dataframe from the data in Data.csv file which contains the responder's data.
For the proof of concept the 'random' and 'indian-cities' library is used to fill in the answers corresponding to each response.

All the data is automatically filled in the google form one at a time. 
After each response is submitted, the script automatically intercepts and chooses to fill the next response.
