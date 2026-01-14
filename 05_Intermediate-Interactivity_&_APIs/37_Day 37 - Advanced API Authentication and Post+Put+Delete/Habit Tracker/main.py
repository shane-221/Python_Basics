#---------------------------------------------Import functions---------------------------------------------------------#
import requests
from datetime import datetime


#-----------------------------------------------Constants--------------------------------------------------------------#
TOKEN = "qwertyuiop1998!"
USERNAME = "shane98"
AGREE_TERMS_OF_SERVICE = "yes"
NOT_MINOR = "yes"
HEADERS= {"X-USER-TOKEN":TOKEN}
GRAPH_ID= "graph1"


#-----------------------------------------------Parameters for the request---------------------------------------------#
# Todo: Getting the user built
url_endpoint= "https://pixe.la/v1/users"
user_params ={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": AGREE_TERMS_OF_SERVICE,
    "notMinor":NOT_MINOR
            }
# Todo: Creating a new graph
graph_endpoint =f"{url_endpoint}/{USERNAME}/graphs"
graph_params ={
    "id":"graph1",
    "name": "Running graph",
    "unit":"KM",
    "type":"float",
    "color": "momiji"
}
# Todo: Adding data into the graph
unit_endpoint =f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
date_format = today.strftsime("%Y%m%d")
unit_params ={
    "date":date_format,
    "quantity":input("How many KM did you run today")
             }

# Todo: Updating datapoints depending on the data
update_endpoint =f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_format}"
update_params ={
    "quantity": "4.5"
                }
# Todo: Deleting a pixel
delete_endpoint =f"{url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_format}"

#-------------------------------------------Post request---------------------------------------------------------------#

requests1= requests.post(url=url_endpoint,json=user_params)
print(request1.text)

#--------------------------------------Post request for a  graph-------------------------------------------------------#
requests2= requests.post(url=graph_endpoint,json=graph_params, headers= HEADERS)
print(requests2.text)

#----------------------------------------Posting a unit fo data into the graph-----------------------------------------#
requests3=requests.post(url =unit_endpoint, json= unit_params, headers= HEADERS)
print(requests3.text)

#----------------------------------------Updating a Pixel--------------------------------------------------------------#
requests4=requests.put(url =update_endpoint, headers= HEADERS)
print(requests4.text)

#--------------------------------------------Deleting a pixel ---------------------------------------------------------#
requests5=requests.put(url =update_endpoint, json= update_params, headers= HEADERS)
print(requests5.text)