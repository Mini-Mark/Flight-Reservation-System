import json

class Account:
    
    def login(self,username,password):
        fdata = open("D:/It's me Hans/Json/user.json")
        data = json.load(fdata)
        self.username = username
        self.password = password
        for i in data['user']:
            l=i["username"] 
            if self.username == l:
                for y in data['user']:
                        y=y["password"]
                        if self.password == y and self.username == l:
                                return i['id']
        
        return False
        
    def register(self,username,password,id_card,phone):
        self.username = username
        self.password = password
        self.id_card = id_card
        self.phone = phone
        data = {}
             
        with open ("D:/It's me Hans/Json/user.json") as json_file:
            data = json.load(json_file)
            y = len(data["user"])+1
            p={"id":y,"username":self.username, "password":self.password, "id_card":self.id_card, "phone":self.phone}

            
            for i in data["user"]:
                check_user = i["username"]
                print(check_user)
                if self.username == check_user:
                    print (self.username)
                    return False

            data["user"].append(p)

            with open ("D:/It's me Hans/Json/user.json", "w") as f:
                json.dump(data, f, indent=4)
    

class User():
    def __init__(self,user_id):
        data = User.getUserById(user_id)
        self.id = data['id']
        self.username = data ['username']
        self.id_cart = data ['id_card']
        self.phone = data ['phone']
        
    @staticmethod
    def getUserById(id):
        fdata = open("D:/It's me Hans/Json/user.json")
        data = json.load(fdata)
        for i in data['user']:
            y=i['id']
            if str(y) == str(id):
                return {"id":i['id'],"username":i['username'],"id_card":i['id_card'],"phone":i['phone']}
        return False
    
    def searchFlight(self,source,destination):
        self.source = source
        return Flight.getFlightByDestination(destination)

class Guest(User):
    def __init__(self):
        super().__init__(0)

class Flight():
    @staticmethod
    def getFlightByDestination(destination):
                fdata = open("D:\It's me Hans\Json\Destination-Flight.json")
                data = json.load(fdata)

                try:
                        a = data['Destination'][destination]
                except:
                        return False

                return a 

    @staticmethod
    def getFlightById(id):
                fdata = open("D:\It's me Hans\Json\Destination-Flight.json")
                data = json.load(fdata)
                id = id
                for i in data['Destination']:
                        for e in data['Destination'][i]:
                                y=e['id']
                                if y == id:
                                        return {"id":e['id'],"name":e['name'],"start":e['start'],"end":e['end'],"price":e['price']}
                return False
    
class Source():
    @staticmethod
    def getAllSource():
        source_list = []
        with open ("D:\It's me Hans\Json\Source-Flight.json") as json_file:
            data = json.load(json_file)
            for i in data["Source"]:
                source_list.append(i)
            return source_list
class Destination():
    @staticmethod
    def getAllDestination():
        destination_list = []
        with open ("D:\It's me Hans\Json\Destination-Flight.json") as json_file:
            data = json.load(json_file)
            for i in data["Destination"]:
                destination_list.append(i)
            return destination_list

class Book_Flight():
    
    def __init__(self,id):
        data = self.getBookDetailById(id)
        self.Book_id = id
        self.Flight_ID: data["Flight_ID"]
        self.Source: data["Source"]
        self.Destination: data["Destination"]
        self.User_ID: data["User_ID"]
        self.Status: data["Status"]
    
    @staticmethod
    def book(Source,Destination,Flight_ID,User_ID,Status):
        fdata = open("D:\It's me Hans\Json\Book.json")
        fdata = json.load(fdata)
        count = 1
        
        for i in fdata:
            count += 1
        p={str(count): {"Flight_ID": str(Flight_ID),"Source": str(Source),"Destination":str(Destination),"User_ID": str(User_ID),"Status": str(Status)}}
        fdata.update(p)
        
        sourch_file = open("D:\It's me Hans\Json\Book.json", "w")
        json.dump(fdata, sourch_file, indent=6)
        return str(count)
    
    
    def pay(self):
        self.Status = "Complete"

        with open ("D:\It's me Hans\Json\Book.json") as json_file:
            data = json.load(json_file)
            data[str(self.Book_id)]["Status"] = self.Status
            sourch_file = open("D:\It's me Hans\Json\Book.json", "w")
            json.dump(data, sourch_file, indent=4)
            
    def cancel(self):
        self.Status = "Cancel"

        with open ("D:\It's me Hans\Json\Book.json") as json_file:
            data = json.load(json_file)
            data[str(self.Book_id)]["Status"] = self.Status
            sourch_file = open("D:\It's me Hans\Json\Book.json", "w")
            json.dump(data, sourch_file, indent=4)
    
    def getDetail(self):
        return Book_Flight(self.Book_id)
    
    @staticmethod
    def getBookDetailById(book_id):
        fdata = open("D:\It's me Hans\Json\Book.json")
        data = json.load(fdata)
        for i in data:
                if str(i) == str(book_id):
                        return data[i]
        return False
    
    @staticmethod
    def getBookHistoryByUserId(user_id):
        fdata = open(".D:\It's me Hans\Json\Book.json")
        data = json.load(fdata)
        dic = []
        for i in data:
                if str(user_id) == str(data[i]['User_ID']):
                        dic.append(data[i])
        return dic
    @staticmethod
    def getAllBookData():
        fdata = open("D:/It's me Hans/Json/Book.json")
        data = json.load(fdata)
        count = 0
        for i in data:
            count += 1
        return count

    
    
class Ticket():
    def __init__(self,book_id):
        with open (".D:\It's me Hans\Json\Book.json") as json_file:
            data = json.load(json_file)
            
            self._user_data = User.getUserById(data[book_id]["User_ID"])
            self._destination_data = Flight.getFlightById(data[book_id]["Flight_ID"])
            self._source = data[book_id]["Source"]
    
    @property
    def user_data(self):
        return self._user_data
    
    @property
    def destination_data(self):
        return self._destination_data
    
    @property
    def source(self):
        return self._source

# Han = Source()
# Han.getsource('hatyai')
# Han = Book_Flight(1)
# print (Han.getAllBookData())
# Han.book('bankok','Hatyai','01-HDY','1','pending')