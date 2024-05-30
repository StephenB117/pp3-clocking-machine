import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")

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
            print("Badge valid")
            break
    return badge

def validate_user_input(data):
    """
    Inside the try, converts all string values into integers,
    Raises ValueError is strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(nums) for nums in data]
        if len(data) != 4:
            raise ValueError(f"Badge number must be 4 numbers you have entered {len(data)}")

    except ValueError as e:
        print(f"invalid data: {e} please enter a number\n")
        return False

    return True 





test = get_badge_number()
