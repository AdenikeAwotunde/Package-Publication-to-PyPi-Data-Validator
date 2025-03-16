import pytest
import datetime
import sys
import os

# Adding the parent directory of the package 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data_Validator_Package.data_validator import DataValidator

@pytest.fixture
def test_DataValidator():
    """Fixture to initialize DataValidator with valid test data"""
    return DataValidator(
        email="awotundeadenike@outlook.com",
        phone_no="+2348092456756",
        date="05-02-1999",  
        url="https://google.com"
    )

"""Email Validation Tests"""
# Test with a valid email
def test_validate_email_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_email() == True

# Test with an invalid email
def test_validate_email_with_invalid_data():
    validator = DataValidator(email="awotunde.com", phone_no="+2348092456756", date="05-02-1999", url="https://google.com")
    assert validator.validate_email() == False


"""Phone Number Validation Tests"""
# Test with a valid phone number
def test_validate_phone_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_phone() == True

# Test with an invalid phone number
def test_validate_phone_with_invalid_data():
    validator = DataValidator(email="awotundeadenike@outlook.com", phone_no="ab132490", date="05-02-1999", url="https://google.com")
    assert validator.validate_phone() == False


"""Date Validation Tests"""
# Test with a valid date format
def test_validate_date_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_date() == True

# Test with an invalid date format
def test_validate_date_with_invalid_data():
    invalid_dates = ["02012000", "12/21/1990", "55/02/1990"]  # Invalid formats
    for date in invalid_dates:
        validator = DataValidator(email="awotundeadenike@outlook.com", phone_no="+2348092456756", date=date, url="https://google.com")
        assert validator.validate_date() == False


"""URL Validation Tests"""
# Test with a valid URL
def test_validate_url_with_valid_data(test_DataValidator):
    assert test_DataValidator.validate_url() == True

# Test with an invalid URL
def test_validate_url_with_invalid_data():
    invalid_urls = ["biggle.co", "www@biggle.co", "http.biggle.com"]
    for url in invalid_urls:
        validator = DataValidator(email="awotundeadenike@outlook.com", phone_no="+2348092456756", date="05-02-1999", url=url)
        assert validator.validate_url() == False