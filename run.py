import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pp3-clocking-machine")

def get_badge_number():
    """
    Gets the users badge number from the user via the terminal.
    Badge number must only contain numbers in the range of 0001 to 9998.  
    """
    while True:
        badge = input("Please enter your clocking number or enter 9999 to register as a new user\n")
        if validate_user_input(badge):
            print("Input valid")
            break
    return badge

def validate_user_input(data):
    """
    Inside the try, converts all string values into integers,
    Raises ValueError is strings cannot be converted into int,
    or if there aren't exactly 4 values.
    """
    try:
        [int(nums) for nums in data]
        if len(data) != 4:
            raise ValueError(f"Badge number must be 4 numbers you have entered {len(data)}")

    except ValueError as e:
        print(f"invalid data: {e} please enter a number\n")
        return False

    return True 

def new_or_current_user(data):
    """
    Checks if the user has entered 9999 to register as a new user. Or if they are a current user.
    If they are a new user they are asked to enter their desired badge number. This is then added to the sheet
    If they are a returning user they are checked against the google sheet. 
    """
    current_badges = SHEET.worksheet("badge_numbers").col_values(1)
    if data == "9999":
        new_badge = input("Please enter your desired badge number\n")

        while True:
            if new_badge in current_badges:
                print("This badge is current unavailable please try again\n")
                new_badge = input("Please enter your desired badge number\n")
            else:
                print(f"This badge is available. Your new badge number is {new_badge}\n")
                SHEET.worksheet("badge_numbers").append_row([new_badge])
                print("Badge number added to database\n")
                break

    else:
        while True:
            if data in current_badges:
                print("Welcome back\n")
                break
            else:
                print("Badge number does not exist\n")
                data = input("Please enter your badge number again\n")

def record_clocking():
    clockings = SHEET.worksheet("clockings")




test = get_badge_number()
new_or_current_user(test)

# create two functions in new or current user to handle each situation and run them in a while loop 
# so main function then while create new user//check is user exists break 
#add each new clocking to its own row with badge number in cell 1 in time in cell 2 
#figure out how to add a clock out time to the third cell 
#