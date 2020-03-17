#!/usr/bin/env python3
"""
Created on Tue Mar  3 12:33:35 2020

@author: janwillem
"""

import time
import requests
import json
from influxdb import InfluxDBClient


token_url_external = "http://5.159.33.181/api/rt/v1/TokenProvider/get_token"
token_url_internal = "http://192.168.0.10/api/rt/v1/TokenProvider/get_token"

connection_url_external = "http://5.159.33.181/api/rt/v1/connection/create"
connection_url_internal = "http://192.168.0.10/api/rt/v1/connection/create"

get_connection_status_url_external = "http://5.159.33.181/api/rt/v1/connection/status?token=8e89020d-67a6-4bc8-9435-6c67931a5a3c"
get_connection_status_url_internal = "http://192.168.0.10/api/rt/v1/connection/status?token=8e89020d-67a6-4bc8-9435-6c67931a5a3c"

get_counts_url_external = "http://5.159.33.181/api/rt/v1/counts/countspage?token=85333f2a-d682-4902-8536-66883ac39d8f&newestFirst=true"
get_counts_url_internal = "http://192.168.0.10/api/rt/v1/counts/countspage?token=802e16f9-a47b-48b9-a5ce-04995ca8354e&newestFirst=true"


get_counts_from_to_url_external = "http://5.159.33.181/api/rt/v1/counts/countspagebetween?token=802e16f9-a47b-48b9-a5ce-04995ca8354e&from=2020-03-10T9:42:26.159Z&to=2020-03-10T14:42:26.159Z"
get_counts_from_to_url_internal = "http://192.168.0.10/api/rt/v1/counts/countspagebetween?token=085aa273-8877-49d9-b0ae-7413e020f3b8&from=2020-03-10T9:42:26.159Z&to=2020-03-10T14:42:26.159Z"

get_counts_max_amount_of_entries_url_external = "http://5.159.33.181/api/rt/v1/counts/countspagerange?token=085aa273-8877-49d9-b0ae-7413e020f3b8&count=4&nextIndex=1735"
get_counts_max_amount_of_entries_url_internal = "http://192.168.0.10/api/rt/v1/counts/countspagerange?token=f5f68c69-9f6f-4852-bf0c-751e718c9419&count=4"


# Once
def create_token(url):
    payload = "\"043281cd-91de-4f5a-b0a4-0805965f0afc\""
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4Mzg0MzAxMCwiZXhwIjoxNTgzODQ2NjEwLCJpYXQiOjE1ODM4NDMwMTAsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.eXjeCck53St4n6rBMPxBSdOi_ufzLvNDBZJEgY6tgfw',
  'Content-Type': 'application/json'
}

    response = requests.request("POST", url, headers=headers, data = payload)
    
# To do: put response in to a variable which can be provided to the url's.
    print(response.text.encode('utf8'))
    

# Create connection with the people counter
def create_connection(connection_url):
    payload = "{\n    \"Device\": \"direct\",\n    \"Live\": \"true\"\n}"
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4NDQ1MDA0MCwiZXhwIjoxNTg0NDUzNjQwLCJpYXQiOjE1ODQ0NTAwNDAsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.ocyGcJ2eyAqaMnEIYVenOTTUZHLCWSJPiKDNrn7DfZ0',
  'Content-Type': 'application/json'
}

    response = requests.request("POST", connection_url, headers=headers, data = payload)

    print("Create connection: ", response.text.encode('utf8'))

# Get connection status data    
def get_connection_status(status_url):
    payload = {}
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4NDQ1MDA0MCwiZXhwIjoxNTg0NDUzNjQwLCJpYXQiOjE1ODQ0NTAwNDAsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.ocyGcJ2eyAqaMnEIYVenOTTUZHLCWSJPiKDNrn7DfZ0'}
    response = requests.request("GET", status_url, headers=headers, data = payload)

    print(response.text.encode('utf8')) 

# Get total amount of ingoing customers   
def get_counts(get_counts_url):
    payload = {}
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4NDQ1MDA0MCwiZXhwIjoxNTg0NDUzNjQwLCJpYXQiOjE1ODQ0NTAwNDAsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.ocyGcJ2eyAqaMnEIYVenOTTUZHLCWSJPiKDNrn7DfZ0'
}

    response = requests.request("GET", get_counts_url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    print("Json: ", response.json())
    
    client = InfluxDBClient('64.227.64.221', 8086, 'admin', 'supersecretpassword', 'telegraf')

    with open('17-3-2020.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)



# Probably unnecessary
def get_counts_from_to(get_counts_from_to_url):
    payload = {}
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4Mzg0MzAxMCwiZXhwIjoxNTgzODQ2NjEwLCJpYXQiOjE1ODM4NDMwMTAsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.eXjeCck53St4n6rBMPxBSdOi_ufzLvNDBZJEgY6tgfw'
}

    response = requests.request("GET", get_counts_from_to_url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    print("Json: ", response.json())
    
    with open('data_from_to.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

# Get the four latest entries. These latest entries will provide ingoing customer data of the latest hour.
def get_counts_max_amount_of_entries(get_counts_max_amount_url):
    payload = {}
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiU3lzdGVtQWRtaW4iLCJzdWIiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsIm5iZiI6MTU4Mzg1MTYxNSwiZXhwIjoxNTgzODU1MjE1LCJpYXQiOjE1ODM4NTE2MTUsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3QifQ.gpjP6UUDoECVHkB4WF9756zOzP2tYFtn4aGOPxNLbyA'
}

    response = requests.request("GET", get_counts_max_amount_url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    print("Json: ", response.json())
    
    with open('data_max_amount_of_entries.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
        
def main():
    #create_token(token_url_external)
    time.sleep(1)
    create_connection(connection_url_external)
    get_connection_status(get_connection_status_url_external)
    time.sleep(1)
    get_counts(get_counts_url_external)


if __name__ == "__main__":
    main()