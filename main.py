import requests
import json
import time

url = "http://localhost:8000/api"

print("------+------+-----+------+-----+-----+-----+------+------")
print("                TChatBot Session Initializing......")
print("------+------+-----+------+-----+-----+-----+------+------\n")
print("TChatBot Session started at : {} ".format(time.ctime()))
print("Type \'quit\' to end chat session")
print("\n------+------+-----+------+-----+-----+-----+------+------")
time.sleep(1)
print("\nTChatBot (Bot): Hey! I'm TChatBot :)")   #This will be done in the JS Backend by default

while True:
    
    input_data = input("\nUser (Human): ")

    if(str(input_data).lower()=='quit'):
        print("------+------+-----+------+-----+-----+-----+------+------")
        print("                TChatBot Session Expiring......")
        print("------+------+-----+------+-----+-----+-----+------+------")
        print("Exited Chat Session....")
        print("------+------+-----+------+-----+-----+-----+------+------\n")
        exit()

    data = json.dumps({"input":input_data})
    r = requests.post(url,data)
    out = r.json()["reply"]
    print("TChatBot (Bot): {}".format(out))