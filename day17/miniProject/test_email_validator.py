from email_validator import validate_email

def test_valid_email():
    assert validate_email("test@gmail.com")==True
def test_missing_at():
    assert validate_email("testgmail.com")==False
def test_missing_dot():
    assert validate_email("test@gmailcom")==False
def test_username_missing():
    assert validate_email("@gmail.com")==False
def test_missing_domain():
    assert validate_email("test@.com")==False
