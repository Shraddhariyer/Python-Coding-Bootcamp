#to generate random quotes
import requests

url="https://dummyjson.com/quotes/random"

response=requests.get(url)
if response.status_code==200:
    data=response.json()
    quote=data["quote"]
    author=data["author"]
    print("\nRANDOM QUOTES GENERATOR\n")
    print("Quote: ",quote)
    print("Author: ",author)
else:
    print("Error occured",response.status_code)