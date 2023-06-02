import json
from lib.json_ext import (
    check_spam_email,
    is_ip_abuse,
    json_to_csv
)

# def test_check_spam_email():

#     assert check_spam_email("me@yopmail.com") == True
#     assert check_spam_email("ceo@google.com") == False
#     assert check_spam_email("example.com") == None

def test_is_ip_abuse():

    with open("config.json") as f:
        data = json.load(f)
        token = data.get("token")
    
    ip_address_1 = "118.25.6.39" # Tencent IP from Documentation
    ip_address_2 = "104.28.233.75" # Random spam IP I gathered from a database
    ip_address_3 = "138.201.206.82" # Oxide Host Server @ Falkenstein

    assert is_ip_abuse(ip_address_1, token, 1) == False 
    assert is_ip_abuse(ip_address_2, token, 1) == True 
    assert is_ip_abuse(ip_address_2, "fgkjhdfgkjhdfg", 1) == None # Will return none due to invalid API key
    assert is_ip_abuse(ip_address_3, token, 1) == False

def test_json_to_csv():
    filename = "test_data.json"

    new_file = json_to_csv(filename)

    with open(new_file, "r") as f:
        data = f.read().splitlines()

    assert data[0] == "Name,Age,Occupation,Location"
    assert "Bob,22,Social" in data[1]


