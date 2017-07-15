import requests

data = [{"query":"justin gawrilow","num_pages":1,"language":"english"}]

response = requests.post("http://localhost:7777/get_urls",json=data)

print response.text
