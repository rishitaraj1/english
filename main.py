from pywebio import config, session
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import json

def insults():

    with open("json_test.json") as file:
        data = json.load(file)

    put_markdown('# Shakespeare insults😉')

    first_initial = input("Use your first initial to find the first part of your insult.")
    put_text("Thou "+data['first_initial'][0][first_initial]).style("background-color: #B6D0E2; text-align: center; font-family: Times New Roman; font-weight: bold;font-size: 30px;")

    second_initial = input("Your middle initial or the last letter of your first name will give the middle part of your insult")
    put_text(data['middle_initial'][0][second_initial]).style("background-color: #B6D0E2; text-align: center; font-family: Times New Roman; font-weight: bold;font-size: 30px;")

    last_initial = input("Finish your insult by using the first letter of your last name.")
    put_text(data['last_name'][0][last_initial]).style("background-color: #B6D0E2; text-align: center; font-family: Times New Roman; font-weight: bold;font-size: 30px;")

if __name__ == '__main__':
    #insults()
    start_server(insults, port=80)


#start_server(applications,port=32420, debug=True)
