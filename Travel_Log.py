travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#fuction with dictionary
a = {
  "country": "",
  "visits": "",
  "cities": ""
}
def add_new_country(q,w,e):
    a["country"] = q
    a["visits"] = w
    a["cities"] = e
    travel_log.append(a)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)