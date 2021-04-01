import requests
import json


def api_request(mac):
    #set of standard error codes provided by macaddress.io
    error_codes = [400, 401, 402, 422, 429, 500]
    #personal API key given upon sign up. Normally should be in encrypted file
    key = 'at_4tLdoIAuLdO7h8AKV5q4VNeTaj3Bc'
    #the url that we will send the request to. Place key and mac in the string
    url = 'https://api.macaddress.io/v1?apiKey={!s}&output=json&search={!s}'.format(key, mac)
    #define maximum number of retries
    retry = 0
    max_retries = 3
    if retry <= max_retries:
        try:
            r =requests.get(url)
        except Exception as e:
            print(e)
            retry += 1
    #check the request status code
    if r.status_code in error_codes:
        print('Response Error {}. Please try again!'.format(r.status_code))
        return
    returned_data = json.loads(r.text)
    #see if the data is in expected format (dict)
    if not bool(returned_data):
        print("The returned data is not in expected format. Please try again!")
        return
    company_name = returned_data.get('vendorDetails').get('companyName')
    if len(company_name) == 0:
        print('No company information for MAC address {}'.format(mac))
    else:
        print('Company: {}'.format(company_name))
    

if __name__ == '__main__':
    mac = input("Please enter a MAC address using delimiter (':' or '.' or none at all):")
    if len(mac) < 6:
        mac = input('6 or more characters required! Please try again: ')
    api_request(mac)