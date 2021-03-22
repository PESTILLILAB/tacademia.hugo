from sys import exit
import json


with open('static/assets/team.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

for x in obj:
    # print(obj[''+x])
    team_type = obj[x]['type']
    ORCID_gen = obj[x]['ORCID']
    if(ORCID_gen == True):
        ORCID_id = obj[x]['id']

    image = obj[x]['image']
    print(obj[x]['externals'])
    
    for y in obj[x]['externals']:
        print(y)
        print(obj[x]['externals'][y])



    # with open('content/team/'+x.replace(" ", "")+".md", 'w') as myfile:
    #     f.write("---")
    #     f.write("type :")
    # data=myfile.read()



exit()