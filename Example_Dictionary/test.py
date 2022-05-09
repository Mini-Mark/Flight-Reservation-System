import json
 
with open('data/flight_des.json') as json_file:
    data = json.load(json_file)
 
    print("Name:",data["Destination"]["Phitsanulok"])
    
    print("--------------------------")
    for i in data["Destination"]["Phitsanulok"]:
        print("ID:",i["Id"])
        print("Time_Start:",i["Time_Start"])
        print("Time_End:",i["Time_End"])
        print("Price:",i["Price"])
        print("--------------------------")
    
    # print("Name:",data["Destination"]["Bankok"])