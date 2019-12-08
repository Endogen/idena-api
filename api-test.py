from api import IdenaAPI


api = IdenaAPI()

'''
result = api.balance("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Balance:", result["data"]["balance"])

result = api.transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Transactions:", result["data"]["transactions"])

result = api.pending_transactions("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 10)
print("Pending Transactions:", result["data"]["transactions"])

result = api.kill_identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Identity Killed:", result["data"])

result = api.go_online()
print("Go Online:", result["data"])

result = api.go_offline()
print("Go Offline:", result["data"])

result = api.send("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", "0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74", 1)
print("Send:", result["data"])

result = api.sync_status()
print("Sync Status:", result["data"])

result = api.node_version()
print("Node Version:", result["data"])

result = api.identities()
print("Fetch Identities:", result["data"])

result = api.identity("0x18a5eb84dc215a2f170ff1f78dc1873ed8d04d74")
print("Fetch Identity:", result["data"])

result = api.epoch()
print("Epoch:", result["data"])

result = api.ceremony_intervals()
print("Ceremony Intervals:", result["data"])

result = api.address()
print("Coinbase Address:", result["data"])
'''
