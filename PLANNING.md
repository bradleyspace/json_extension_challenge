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

## Getting data using an api key

Parameters: 
- [x] `ip` The IP address to check
- [x] `api_key` The authorisation key
- [x] `max_attempts` 

Returns:
- [x] `Tuple[bool, dict]` - A boolean representing if the test was valid and a dict resprensting the data returned, if any.

Function:
- [x] Send the request using an API key and some test data
- [x] Check to see if the request code was successful
- [x] Serialize the json data returned into a dict
- [] Return the tuple containing the boolean and dictionary

## Converting JSON to CSV
Parameters:
- []

