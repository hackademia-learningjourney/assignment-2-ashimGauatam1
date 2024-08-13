
import json

dict1={
    "username":[],
    "password":[],
    "mobile":[]
}

print("1:Sign up")
print("2: Sign in")

x=int(input("enter your choice\n"))
match x:
    case 1:
        with open("auth.json","w") as f:
            username=input("enter username\n")
            password=input("enter password\n")
            mobile_number=int(input("enter your mobile numeber\n"))
            dict1["username"].append(username)
            dict1["password"].append(password)
            dict1["mobile"].append(mobile_number)
            json.dump(dict1,f)
        
    case 2:
        with open("auth.json",'r') as f:
            username=input("enter your username\n")
            password=input("enter your password\n")
            out=json.load(f)
            if username in out["username"]:
                if password in out["password"]:
                    print(f'welcome {username}')
                else:
                   print("invalid credentials")    
            else:
                print("invalid credentials")


