import scratchattach as scratch
import json
import datetime
import os

login = scratch.login("likeIcare2022_", os.environ["PASSWORD"])
conn = login.connect_cloud("1058102705")
project = login.connect_project(1058102705)
alphabet = ['', '', '', '', '', '', '', '', '', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_']
username = ''
data = ''
encoded = ''
decoded = ''


def encode(text):
    global encoded
    encoded = ''
    idx = 0
    for i in range(len(text)):
        letter = text[idx].upper()
        list_index = alphabet.index(letter)
        encoded = encoded + str(list_index)
        idx += 1

    return encoded


def decode(encoded_str):
    idx = 0
    lnumbers = []
    while idx < len(encoded_str):
        number = int(encoded_str[idx:idx + 2])
        lnumbers.append(number)
        idx += 2

    global decoded
    decoded = ''
    for num in lnumbers:
        letter = alphabet[num]
        decoded = decoded + letter

    return decoded


while True:
    if not scratch.get_var("1058102705", "PING") == "0":
        conn.set_var("PING", "0")
        print("pinged")
    try:
        if not scratch.get_var("1058102705", "USERNAME") == "0" and not scratch.get_var("1058102705", "USERNAME") is None:
            data = json.loads(open('data.json', 'r').read())
            print(data)
            username = scratch.get_var("1058102705", "USERNAME")
            conn.set_var("USERNAME", "0")
            if not decode(username) in data and not decode(username) == '':
                data[decode(username)] = [{'coins': 100}, {'joined': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]
                print(data)
                with open('data.json', 'w') as file:
                    file.write(json.dumps(data))
            elif not decode(username) == '':
                print(data[decode(username)][0]['coins'])
                conn.set_var('COINS', str(data[decode(username)][0]['coins']))
    except:
        print("Login Failed")
    try:
        if not scratch.get_var("1058102705", "SENDER") == '0' and not scratch.get_var("1058102705", "SENDER") is None:
            data = json.loads(open('data.json', 'r').read())
            amount = scratch.get_var("1058102705", "AMOUNT")
            user = decode(scratch.get_var("1058102705", "USER"))
            sender = decode(scratch.get_var("1058102705", "SENDER"))
            conn.set_var('SENDER', '0')
            conn.set_var('USER', '0')
            conn.set_var('AMOUNT', '0')
            print(sender, amount, user)
            if not sender == '' and data[sender][0]['coins'] >= int(amount):
                data[user][0]['coins'] = data[user][0]['coins'] + int(amount)
                data[sender][0]['coins'] = data[sender][0]['coins'] - int(amount)
                with open('data.json', 'w') as file:
                    file.write(json.dumps(data))
    except:
        print('Transaction Failed')
