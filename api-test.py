from api import IdenaAPI


api = IdenaAPI()
'''
result = api.balance("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Balance:", result["result"]["balance"])

result = api.transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Transactions:", result["result"]["transactions"])

result = api.pending_transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Pending Transactions:", result["result"]["transactions"])

result = api.kill_identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Identity Killed:", result["result"])

result = api.go_online()
print("Go Online:", result["result"])

result = api.go_offline()
print("Go Offline:", result["result"])

result = api.send("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", "0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 1)
print("Send:", result["result"])

result = api.sync_status()
print("Sync Status:", result["result"])

result = api.node_version()
print("Node Version:", result["result"])

result = api.identities()
print("Fetch Identities:", result["result"])

result = api.identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Fetch Identity:", result["result"])

result = api.epoch()
print("Epoch:", result["result"])

result = api.ceremony_intervals()
print("Ceremony Intervals:", result["result"])
'''
result = api.address()
print("Coinbase Address:", result["result"])
