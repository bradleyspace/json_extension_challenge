# Plannning

## Fetching data from APIs

API: [Mailcheck](https://mailcheck.ai)

#### Description:

A simple function that checks whether a email is from a "disposable" email service, like yopmail or similar.

#### Requirements

Parameters (1):
- [x] `email` - The email parameter that we will send to the API

Returns:
- [x] Boolean - True or False depending on if the email is disposable or not

Function:
- [x] Split the domain - Checkmail takes the domain of the email, not the full email
- [x] Send the API request
- [x] Parse the JSON data
- [x] Return a boolean value
- [x] Write test to validate

## Getting data using an api key

Parameters: 
- [x] `ip` The IP address to check
- [x] `api_key` The authorisation key
- [x] `max_reports` - The amount of reports needed to be considered "abusive"

Returns:
- [x] `Union[Bool, None]` - A boolean representing if the IP is considered "abusive", None is returned if the API Key or IP address is invalid.

Function:
- [x] Send the request using an API key and some test data
- [x] Check to see if the request code was successful
- [x] Serialize the json data returned into a dict
- [] Return the tuple containing the boolean and dictionary
- [x] Write test to validate

## Converting JSON to CSV

Parameters:
- [x] `filename` - The JSON file to load

Returns:
- [x] `str` - The filename of the CSV file generated

Function:
- [x] Load the JSON file and get the appropriate keys
- [x] Create a CSV file and open it in write mode
- [x] Append the keys to the top row
- [x] Iterate through the JSON file and add the values as CSV entries
- [x] Write test to validate
