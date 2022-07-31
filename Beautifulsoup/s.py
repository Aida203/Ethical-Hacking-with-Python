import requests
from bs4 import BeautifulSoup

pageCounter = 0
urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=php&start={pageCounter}")
# save html content

markup = urlResult.content

# take object from beautiful soup
bs = BeautifulSoup(markup , 'lxml')

# find h2 from markup
jobHeadings = bs.find_all('h2' , {"class" : "css-m604qf"})
jobAnchors = bs.find_all('a' , {"class" : "css-o171kl"})
jobLocation = bs.find_all('span' , {"class" : "css-5wys0k"})
experienceYears=bs.find_all('div',{"class":"css-4c4ojb"})


# create list to append all jobs 
jobs = []

for i in range(14): #to loop through all pages
    for i in range(len(experienceYears)):  #to print the content
        jobs.append(jobHeadings[i].text)
        jobs.append(jobLocation[i].text)
        jobs.append(experienceYears[i])
        jobs.append("------------------------------------------")
    

for i in jobs:
    print(i)
    print("\n")




