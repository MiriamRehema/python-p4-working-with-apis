
import requests
import json


class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.text   #i have commented it out since it will return the API in not a friendly way and used the dumps method
    json_content = json.loads(response.text)
    print(json.dumps(json_content, indent=4, sort_keys=True))

  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
            programs_list.append(program["agency"])

    return programs_list
#comment this out
#programs = GetPrograms().get_programs()
#print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)

