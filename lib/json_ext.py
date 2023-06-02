import requests
import json

# A function which uses the MailCheck API to 
# determine if the origin domain of an email address
# is disposable
# Parameters:
# - Name: email
# - Definition: A string containing the email
# Returns:
# - Boolean

MAILCHECK_URI = "https://api.mailcheck.ai/domain/"
ABUSEIPDB_URI = "https://api.abuseipdb.com/api/v2/check"

def check_spam_email(email: str) -> bool:
    # Strip out the domain from the email string.

    domain = email.split("@")

    if len(domain) < 2:
        return None
    
    domain = domain[1]

    # Send the request to the API by joining the API 
    # URL and the domain from the parameter together
    # This will look something like: "https://api.mailcheck.ai/domain/example.com"

    res = requests.get(f"{MAILCHECK_URI}{domain}")

    # Convert the data to JSON

    data = res.json()

    is_disposable = data["disposable"]

    return is_disposable

# A function which checks if a specified IP address is blocked
# Parameters
# - Name: ip
# - Type: str
# - Description: The specified IP address to check
#
# - Name: token
# - Type: str
# - Description: The API token to authorise the request to AbuseIPDB
#
# - Name: max_reports
# - Type: int
# - Description: The maximum amount of reports to be considered "abusive"
#
# Returns:
# - Union[bool, None]

def is_ip_abuse(ip: str, token: str, max_reports: int) -> bool | None:
    
    # Request Headers
    headers = {
        "Accept": "application/json",
        "Key": token,
    }

    # Request Query Params
    query = {
        "ipAddress": ip,
    }

    # Create a requests session with a ctx manager
    # This ensures that the socket is closed to free memory
    with requests.Session() as session:
        res = session.get(url=ABUSEIPDB_URI, headers=headers, params=query)

    # Ensure the status code is 200 (AKA: The request/token is valid)
    # Else return None
    if res.status_code != 200:
        return None
    
    # Parse the data into JSON
    data = res.json()

    # Grab the total number of reports
    reports = data["data"]["totalReports"]

    # If reports exceed the maximum number of reports,
    # return True
    if reports >= max_reports:
        return True
    
    # return False
    return False

    
def json_to_csv(filename):

    # Open the JSON file
    with open(filename, "r") as f:
        json_data = json.load(f)

    #

    