import json
from fastapi import HTTPException
import httpx

class TonClient:
    def __init__(self):
        self.base_url = "https://api.shasta.trongrid.io/"

    async def get_tron_address_balance(self, address: str):
      
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        body = {
            "address": address,
            "visible": True
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(self.base_url + "wallet/getaccount", headers=headers, json=body)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
    async def get_tron_address_resources(self, address: str):

      
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        body = {
            "address": address,
            "visible": True
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(self.base_url + 'wallet/getaccountresource', json=body)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
