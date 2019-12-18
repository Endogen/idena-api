import requests


class IdenaAPI:

    _host = "localhost"
    _port = "9009"
    _timeout = 3

    def __init__(self, host=_host, port=_port, timeout=_timeout):
        self._host = host
        self._port = port
        self._timeout = timeout
        self.url = f"http://{host}:{port}"

    def _request(self, url, payload):
        try:
            return requests.post(url, json=payload, timeout=self._timeout).json()
        except Exception as e:
            return {"error": {"message": str(e), "code": 0}}

    def identities(self):
        """ List all identities (not only validated ones) """
        payload = {
            "method": "dna_identities",
            "id": 1
        }
        return self._request(self.url, payload)

    def identity(self, address):
        """ Show info about identity for given address """
        payload = {
            "method": "dna_identity",
            "params": [address],
            "id": 1
        }
        return self._request(self.url, payload)

    def epoch(self):
        """ Details about the current epoch """
        payload = {
            "method": "dna_epoch",
            "id": 1
        }
        return self._request(self.url, payload)

    def ceremony_intervals(self):
        """ Show info about validation ceremony """
        payload = {
            "method": "dna_ceremonyIntervals",
            "id": 1
        }
        return self._request(self.url, payload)

    def address(self):
        """ Show address for current identity """
        payload = {
            "method": "dna_getCoinbaseAddr",
            "id": 1
        }
        return self._request(self.url, payload)

    def balance(self, address):
        """ Show DNA balance for address """
        payload = {
            "method": "dna_getBalance",
            "params": [address],
            "id": 1
        }
        return self._request(self.url, payload)

    def transaction(self, trx_hash):
        """ Details about a specific transaction """
        payload = {
            "method": "bcn_transaction",
            "params": [trx_hash],
            "id": 1
        }
        return self._request(self.url, payload)

    def transactions(self, address, count):
        """ List specific number of transactions for given address """
        payload = {
            "method": "bcn_transactions",
            "params": [{"address": f"{address}", "count": int(count)}],
            "id": 1
        }
        return self._request(self.url, payload)

    def pending_transactions(self, address, count):
        """ List specific number of pending transactions for given address """
        payload = {
            "method": "bcn_pendingTransactions",
            "params": [{"address": f"{address}", "count": int(count)}],
            "id": 1
        }
        return self._request(self.url, payload)

    def kill_identity(self, address):
        """ Kill your identity """
        payload = {
            "method": "dna_sendTransaction",
            "params": [{"type": 3, "from": f"{address}", "to": f"{address}"}],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Not working! Which argument to use?
    def go_online(self, address):
        """ Go online, serve as a valid node and start mining """
        payload = {
            "method": "dna_becomeOnline",
            "params": [address],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Not working! Which argument to use?
    def go_offline(self, address):
        """ Go offline, do not serve as a node and stop mining """
        payload = {
            "method": "dna_becomeOffline",
            "params": [address],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Untested!
    def send_invite(self, to_address, amount):
        """ Send invite code to given address """
        payload = {
            "method": "dna_sendInvite",
            "params": [{"to": to_address, "amount": amount}],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Untested!
    def activate_invite(self, to_address, key):
        """ Send invite code to given address """
        payload = {
            "method": "dna_activateInvite",
            "params": [{"to": to_address, "key": key}],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Untested!
    def flip(self, flip_hash):
        """ Show info about flip by providing his hash """
        payload = {
            "method": "flip_get",
            "params": [flip_hash],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Untested!
    def submit_flip(self, flip_hex, pair_id):
        """  """
        payload = {
            "method": "flip_submit",
            "params": [{"hex": flip_hex, "pair": pair_id}],
            "id": 1
        }
        return self._request(self.url, payload)

    def send(self, from_address, to_address, amount):
        """ Send amount of DNA from address to address """
        payload = {
            "method": "dna_sendTransaction",
            "params": [{"from": from_address, "to": to_address, "amount": amount}],
            "id": 1
        }
        return self._request(self.url, payload)

    def sync_status(self):
        """ Show if node is synchronized """
        payload = {
            "method": "bcn_syncing",
            "id": 1
        }
        return self._request(self.url, payload)

    def node_version(self):
        """ Show node version """
        payload = {
            "method": "dna_version",
            "id": 1
        }
        return self._request(self.url, payload)

    def import_key(self, key, password):
        """ Import private key to manage specific identity """
        payload = {
            "method": "dna_importKey",
            "params": [{"key": key, "password": password}],
            "id": 1
        }
        return self._request(self.url, payload)

    # TODO: Untested!
    def export_key(self, password):
        """ Import private key to manage specific identity """
        payload = {
            "method": "dna_exportKey",
            "params": [password],
            "id": 1
        }
        return self._request(self.url, payload)
