from tkinter import *
import requests
import xmltodict

auth_details = ('bartholdbos@hotmail.com', 'arPaFR_Ds1N-MSaH_cRbxm0eP44g7o0ooxMhgCPsot7SlDypTB2JwQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station='

def find():
    station = station_entry.get()

    response = requests.get(api_url + station, auth=auth_details)
    xml = xmltodict.parse(response.text)
    for train in xml['ActueleVertrekTijden']['VertrekkendeTrein']:
        print(train['EindBestemming'])
        label = Label(master=bottomframe, text=train['EindBestemming'])
        label.pack(fil=X)

root = Tk()

topframe = Frame(master=root)
topframe.pack(side=TOP)

station_entry = Entry(master=topframe)
station_entry.pack(side=LEFT)

station_button = Button(master=topframe, text='Zoek', command=find)
station_button.pack(side=RIGHT)

bottomframe = Frame(master=root)
bottomframe.pack(side=BOTTOM)

root.mainloop()