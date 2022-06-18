import requests

api_key = "bcd1636ecde3c91d868e671ba1bb31a7"
city = "Orlando"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description =  json.get("weather")[0].get("description")
print("Today's forecast is "+description)
temp_min = json.get("main").get("temp_min")
print("The low will be", temp_min)
temp_max = json.get("main").get("temp_max")
print("The high will be", temp_max)