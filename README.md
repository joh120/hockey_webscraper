Hockey stats webscrapper 

This is a webscrapper that takes hockey stats from scrapthissite.com and put them into a csv file.

Objective

The objective was to utilise the request library and the BeautifulSoup library in Python within a 
webscraping project. The scrapthissite allow the use of request and BeautifulSoup Python libraries within this mini project.

Hockey stats webscrapper pseudo code:

This is the pseudo code that i created for the hockey stats webscrapper. 

first i install and imported the bs4, requests and csv libraries in Python.

url is a variable that contains the API endpoint from the scrapthissite.

requests.get(url) is requesting the access to the hockey stats data in order to pull its data 
and use it to create a file.

BeautifulSoup() allowed extract the hockey stat data from the website using its html tags. 

After utilising BeautifulSoup i loop over the hockeys stats data in the table and create a file 
that stores it in a csv format. 



