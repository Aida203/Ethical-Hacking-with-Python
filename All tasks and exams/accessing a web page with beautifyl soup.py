import requests  #to work with urls

from bs4 import BeautifulSoup  #helps parse data

urlResult=requests.get("https://wuzzuf.net/search/jobs/?a=spbg&q=php") #pass the link of the page having all the
                                                                      #info we wish to retrieve

#get html of these links using the html script
#=> save this html content

markup=urlResult.content


#taking an object from beautiful soup to help us access the content we need from the url

#we need the markup here with h2 having a specific class name

bs=BeautifulSoup(markup,'lxml')    #=> (content we want to search in, parser)  
#parser = 'lxml' to help us search in that content

#get all h2's first and we need the class name (in the inspect)

jobHeadings=bs.find_all('h2',{"class":"css-m604qf"})  #if it was id then we'll write it
#the {} part is a json format

print(jobHeadings)

#link at once? get link of the class containning the link itself


#text only inside? not with link?  => iterate in this h2 and take the text in a list

#create list to append all jobs




