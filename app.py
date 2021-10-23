import os
from requests import Session
from dotenv import load_dotenv

load_dotenv()

# From .env file
base_url = os.getenv('base_url')
api_key = os.getenv('api_key')
basic_auth = os.getenv('basic_auth')

class Get:
    # Base API call headers
    def __init__(self):
        self.apiurl = base_url
        self.headers = {
            "Accepts": "application/json",
            "Authorization": "Basic " + basic_auth,
            "Content-Type": "application/json",
            "aw-tenant-code": api_key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    # It is used to get health information for tunnel endpoint.
    def TunnelHealth(self):
        url = self.apiurl + "/mdm/tunnel/health"
        r = self.session.get(url)
        data = r.json()
        return data

    # It is used to get health information for tunnel downstream connectivity.
    def TunnelHealthDs(self):
        url = self.apiurl + "/mdm/tunnel/health/downstream"
        r = self.session.get(url)
        data = r.json()
        return data

    # Retrieves the device count (Total, Security, Ownership, Platforms, Enrollmentstatus)
    def DeployedDevices(self):
        url = self.apiurl + "/mdm/devices/devicecountinfo"
        r = self.session.get(url)
        data = r.json()
        return data