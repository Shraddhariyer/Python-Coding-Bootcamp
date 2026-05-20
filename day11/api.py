#get request
import requests

url="https://www.api.com/user"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print("Data:",data)

else:
    print("Error:",response.status_code)


#post request
import requests

url="https://www.api.com/user"
new_data={
    "name":"Rahul"
}
response=requests.post(url,json=new_data)

if response.status_code==200:
    data=response.json()
    print("Data:",data)

else:
    print("Error:",response.status_code)


#put request
import requests

url="https://www.api.com/user"
update_data={
    "name":"Rahul"
}
response=requests.put(url,json=update_data)

if response.status_code==200:
    data=response.json()
    print("Data:",data)

else:
    print("Error:",response.status_code)



#delete request
import requests

url="https://www.api.com/user"

response=requests.delete(url)

if response.status_code==200:
    print("Data deleted successfully")

else:
    print("Error:",response.status_code)