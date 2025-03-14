import datetime
import re

# creating a class for a personal data validator
class DataValidator:
    def __init__(self):
        """initializing a class for personal data validator
           email: email address of user
           phone: phone number of user
           date: date of birth of user
           url: user's website url
        """
        self.email = None
        self.date = None
        self.phone_no = None
        self.url = None
        
    def set_email(self, email):
        self.email = email

    def set_date(self, date):
        self.date = date

    def set_phone_no(self, phone_no):
        self.phone_no = phone_no

    def set_url(self, url):
        self.url = url
        
        
        # function to validate email
    def validate_email(self):
        """Validating email addresses using regex"""
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.search(email_pattern, self.email):
            return True
        else:
            return False
            
            
        # function to validate phone number
    def validate_phone(self):
        """Validating phone number using regex"""
        phone_pattern = r"\+\d{1,3}\s?\d{3}\s?\d{8}\b"
        if re.search(phone_pattern,self.phone_no):
            return True
        else:
            return False
        
        
         # function to validate date
    def validate_date(self):
        """return false if no date is provided"""
        if not self.date:
            return False
        """Validates the date format using regex"""
        date_pattern =  r"^(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})$"
        if not re.match(date_pattern, self.date):
            return False
        
        # Check f date is in correct format
        formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]
        for fmt in formats:
            try:
                datetime.datetime.strptime(self.date, fmt)
                return True  
            except ValueError:
                continue  
        return False 
        
        
    # function to validate url
    def validate_url(self):
        """Validating url using regex"""
        url_pattern = r"\b(?:https?://|www\.)\S+\b"

        if re.search(url_pattern,self.url):
            return True
        else:
            return False