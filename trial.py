from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import json



def app():

    put_markdown('# Shakespeare insults')

    data = input_group("First initial", [
        input('Use your first initial to find the first part of your insult.', name='name', required=True)
    ])

if __name__ == '__main__':
    start_server(app, port=32420, debug=True)

with open("json_test.json") as file:
    data = json.load(file)

file = json.loads("first_initial")

for name in "first_initial":
    if(first_initial["a"]) == True:
        first_initial = ["initial"]







