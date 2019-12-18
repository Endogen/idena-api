# Python wrapper for IDENA RPC interface

```python
from api import IdenaAPI

# Connect to local node with default settings
api = IdenaAPI()

# Connect to remote node
api = IdenaAPI("123.123.123.123", 9090)

# Check balance
result = api.balance("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")

# Always make sure that response was successful
if "error" in result:
    print(result["error"]["message"])
elif "success" in result:
    print(result["result"])



# Get your balance
result = api.balance("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Balance:", result["result"]["balance"])

# List transactions (specify count of transactions you want to get)
result = api.transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Transactions:", result["result"]["transactions"])

# List pending transacions (specify count of transactions you want to get)
result = api.pending_transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Pending Transactions:", result["result"]["transactions"])

# Kill your identity
result = api.kill_identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Identity Killed:", result["result"])

# Start mining
result = api.go_online()
print("Go Online:", result["result"])

# Stop mining
result = api.go_offline()
print("Go Offline:", result["result"])

# Send DNA
result = api.send("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", "0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 1)
print("Send:", result["result"])

# Check if node is synced
result = api.sync_status()
print("Sync Status:", result["result"])

# Get node version
result = api.node_version()
print("Node Version:", result["result"])

# Get info about all active identities
result = api.identities()
print("Fetch Identities:", result["result"])

# Get info about your identity
result = api.identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Fetch Identity:", result["result"])

# Get info about current epoch
result = api.epoch()
print("Epoch:", result["result"])

# Get info about ceremony intervals
result = api.ceremony_intervals()
print("Ceremony Intervals:", result["result"])

# Get your address
result = api.address()
print("Coinbase Address:", result["result"])
```