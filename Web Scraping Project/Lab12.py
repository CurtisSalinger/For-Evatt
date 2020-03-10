import requests
from bs4 import BeautifulSoup
import json

#Here's a little intro to webscraping. I'm pulling the first 10 pages of ebay when I searched iphone
#Manually get the links

urls = ["https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xiphone.TRS0&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=tools",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=2",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=3"
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=4",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=5",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=6",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=7",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=8",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=9",
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&_pgn=10",
        ]

with open ("items.JSON","w") as TurnIn: #Open or make a file called items that all the results will go into at the end. it is a JSON file
    lst = []
    dtc = {}
    for url in urls:
        r = requests.get(url) #Pull the URL from the internet
        html = r.text #Get the HMTL code from it
        bs = BeautifulSoup(html) #Make a 'Beautiful Soup' object
        listings = bs.find_all("li",class_="s-item") #Find all the items that are Listings. IE ensure we dont search the header, the advertizments, the menu on top etc. the findall function on a beautiful soup object makes a list. You go onto Ebay, inspect element, and find the html tags corresponding to the item. So in list case the tag is: <li>and is class "s-item". So now listings is just a list of all of our items
        for item in listings:
            try: #use this in case there's an error on one of them, ensure it'll keep running even if on gives an error in which case I just append "Error Parsing item" done in line 41
                dtc={}
                price = item.find("span",class_="s-item__price") #again find the html tag that ebay uses to note price, item, condition, etc
                title = item.find("h3",class_="s-item__title")
                condition = item.find("span",class_="SECONDARY_INFO")
                dtc["Name"] = title.text # add them all to our dictionary
                dtc["Price"] = price.text
                dtc["Condition"] = condition.text
                lst.append(dtc) #add the dictionary to the whole list of items
                
            except:
               lst.append("Error Parsing Item")

    json.dump(lst, TurnIn) #This is the command that we give TurnIn contents. In other words, in line 20 we made the file, but it didnt have any contents, untill we 'dump' the lst into the file

	'''
	now go open the items.JSON file and you've got all the iPhones. you can also just add a print(lst) if you want
	'''
