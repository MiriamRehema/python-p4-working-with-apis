
import requests
import json


class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    #return response.text   i have commented it out since it will return the API in not a friendly way and used the dumps method
    json_content = json.loads(response.text)
    print(json.dumps(json_content, indent=4, sort_keys=True))

programs = GetPrograms().get_programs()
print(programs)
