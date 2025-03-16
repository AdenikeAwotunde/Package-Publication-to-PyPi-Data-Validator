import datetime
import re

# creating a class for a personal data validator
class DataValidator:
    def __init__(self, email =None, date = None, phone_no= None, url= None):
        """initializing a class for personal data validator
           email: email address of user
           phone: phone number of user
           date: date of birth of user
           url: user's website url
        """
        self.email = email
        self.date = date
        self.phone_no = phone_no
        self.url = url
        

        
        # function to validate email
    def validate_email(self, verbose =False):
        #Validating email addresses using regex
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_pattern, self.email):
            if verbose:
                print('Email is valid')
            return True
        else:
            return False
            
            
        # function to validate phone number
    def validate_phone(self, verbose = False):
        #Validating phone number using regex
        phone_pattern = r"\+\d{1,3}\s?\d{3}\s?\d{8}\b"
        if re.match(phone_pattern,self.phone_no):
            if verbose:
                print('Phone number is valid')
            return True
        else:
            return False
        
        
    # function to validate date
    def validate_date(self):
        # return false if no date is provided
        if not self.date:
            return False
        """Validates the date format using regex
        date formats supported : DD/MM/YYYY, DD-MM-YYY"""
        
        date_pattern = r"""
    ^(
        (?:31[-/](?:0?[13578]|1[02])) |      # Months with 31 days
        (?:30[-/](?:0?[13-9]|1[0-2])) |      # Months with 30 days
        (?:29[-/]02[-/](?:(?:1[6-9]|[2-9]\d) # 29 days in Feb for leap year
            (?:0[48]|[2468][048]|[13579][26])|2000)) |
        (?:0?[1-9]|1\d|2[0-8])[-/]02 |       # Feb with 28 days
        (?:0?[1-9]|[12]\d|3[01])[-/](?:0?[1-9]|1[0-2]) # General valid dates
    )[-/]\d{4}$                              # End with 4-digit year
"""
        return bool(re.match(date_pattern, self.date, re.VERBOSE))
    
    # Function to validate url
    def validate_url(self, verbose=False):
        """Validates a URL using regex."""
        url_pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/\S*)?$"
        
        if re.match(url_pattern, self.url):
            if verbose:
                print("URL is valid")
            return True
        return False