import pytest
import datetime
import sys
import os

# Adding the parent directory of the package 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data_Validator_Package.data_validator import DataValidator

@pytest.fixture
def test_DataValidator():
    validator = DataValidator()
    validator.set_email("awotundeadenike@outlook.com")
    validator.set_phone_no("+2348092456756")
    validator.set_date("1999-02-05")
    validator.set_url("https://google.com")
    return validator

"""Email Validation Tests"""
# Test with a valid email
def test_validate_email_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_email() == True

#Test with an inalid email
def test_validate_email_with_invalid_data(test_DataValidator):
    validator = DataValidator()
    validator.set_email("awotunde.com")
    assert validator.validate_email() == False


"""Phone Number Validation Tests"""
#Test with a valid phone number
def test_validate_phone_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_phone() == True

# Test with an invalid phone number
def test_validate_phone_with_invalid_data(test_DataValidator):
    validator = DataValidator()
    validator.set_phone_no("ab132490")
    assert validator.validate_phone() == False
    
    
"""Date Validation Tests"""
# Test with a valid date format
def test_validate_date_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_date() == True

#Test with an invalid date format
def test_validate_date_with_invalid_data(test_DataValidator):
    validator = DataValidator()
    
    validator.set_date("02012000") #using invalid format
    assert validator.validate_date() == False
    
    validator.set_date("12/21/1990") # using invalid month
    assert validator.validate_date() == False
    
    validator.set_date("55/02/1990") # using invalid day
    assert validator.validate_date() == False


"""Url Validation Tests"""
#Test with a valid url
def test_validate_url_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_url() == True

#Test with an invalid url
def test_validate_url_with_invalid_data(test_DataValidator):
    validator = DataValidator()
    
    validator.set_url("biggle.co")
    assert validator.validate_url() == False
    
    validator.set_url("www@biggle.co")
    assert validator.validate_url() == False
    
    validator.set_url("http.biggle.com")
    assert validator.validate_url() == False