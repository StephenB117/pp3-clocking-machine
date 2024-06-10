# Clocking Machine
Deployed site https://pp3-clocking-machine-64f1be25171f.herokuapp.com/

This terminal was designed with to simulate how a basic clocking machine works. 

Users can register on the machine if they do not have a badge number or clock in using a registered badge number 

The badge number is checked against the sheet to see if it is valid, if not the user is prompted to try again. 

Once the user is logged into the terminal they will be given the option to clock in or view more options 

If they choose to clock in the clocking time will be displayed to the user and the programme will restart 

If they choose more options they will have the options of viewing their last clocking time, their worked hours for the week and their worked hours for the month. 

## Features:

## My Logic: 
https://lucid.app/lucidchart/98be9683-fe78-4ac7-a0ff-1aff2e83d394/edit?viewport_loc=-1762%2C-306%2C2020%2C948%2C0_0&invitationId=inv_474e441e-4de0-4041-8b93-a76c50c64e4f


## Testing:

## Deployment:
This project was deployed on Heroku using Code Institute's mock terminal

The steps for deployment are as follows: 
- Fork or clone this repository
- Create a new Heroku app
- Set the build packs to Python and NodeJS
- Link the Heroku app to the Github repository
- In settings add a config var with key PORT and value 8000
- In settings add a config car with key CREDS and value the contents of a JSON file to link to a google sheet. 
- Click on deploy

## Credits:

### Content 
Code for connecting to google sheet API's taken from love sandwiches project.

