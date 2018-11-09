import requests
import xmltodict

auth_details = ('bartholdbos@hotmail.com', 'arPaFR_Ds1N-MSaH_cRbxm0eP44g7o0ooxMhgCPsot7SlDypTB2JwQ')

station = input("Vertrekstation: ")

api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station

response = requests.get(api_url, auth=auth_details)
xml = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for train in xml['ActueleVertrekTijden']['VertrekkendeTrein']:
    final_destination = train['EindBestemming']
    train_type = train['TreinSoort']
    departure_track = train['VertrekSpoor']['#text']
    departure_time = train['VertrekTijd']
    departure_time = departure_time[11:16]

    print('Om ' + departure_time + ' vertrekt een ' + train_type + ' naar ' + final_destination + ' van spoor ' + departure_track)