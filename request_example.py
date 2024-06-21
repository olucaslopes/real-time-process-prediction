import requests
import json

url = "localhost:5000/api/v1/predict"

payload = json.dumps({
  "data": [
    {
      "vazaoVapor": 273,
      "pressaoVapor": 57,
      "temperaturaVapor": 718,
      "cargaVaporTG1": 127.5,
      "cargaVaporTG2": 94.875,
      "habilitaTG1": 0,
      "habilitaTG2": 0
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
