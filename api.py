import requests


class IdenaAPI:

    __API_URL = 'http://localhost'
    __API_PORT = "9009"

    def __init__(self, api_url=__API_URL, api_port=__API_PORT):
        self.url = f"{api_url}:{api_port}"

    def balance(self, address):
        payload = {
            "method": "dna_getBalance",
            "params": [f"{address}"],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def transactions(self, address, count):
        payload = {
            "method": "bcn_transactions",
            "params": [{"address": f"{address}", "countd": int(count)}],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def pending_transactions(self, address, count):
        payload = {
            "method": "bcn_pendingTransactions",
            "params": [{"address": f"{address}", "count": int(count)}],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def kill_identity(self, address):
        payload = {
            "method": "dna_sendTransaction",
            "params": [{"type": 3, "from": f"{address}", "to": f"{address}"}],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def go_online(self):
        payload = {
            "method": "dna_becomeOnline",
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def go_offline(self):
        payload = {
            "method": "dna_becomeOffline",
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def send(self, from_address, to_address, amount):
        payload = {
            "method": "dna_sendTransaction",
            "params": [{"from": from_address, "to": to_address, "amount": amount}],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def sync_status(self):
        payload = {
            "method": "bcn_syncing",
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def node_version(self):
        payload = {
            "method": "dna_version",
            "id": 1
        }
        return requests.post(self.url, json=payload).json()

    def import_key(self, key, password):
        payload = {
            "method": "dna_importKey",
            "params": [{"key": key, "password": password}],
            "id": 1
        }
        return requests.post(self.url, json=payload).json()
