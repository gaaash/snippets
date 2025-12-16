import requests

ipdata =  requests.get("https://ifconfig.co/json").json()
print("\n",ipdata['country'], "=====> " , ipdata["ip"], "\n")
