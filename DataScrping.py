print('DataScrping')
import urllib.request
import requests
from bs4 import BeautifulSoup

# URL of the web page to fetch
url=input('Input the URL to scrap - > ')

try:
    # Open the URL and read its content
    response = urllib.request.urlopen(url)
    
    # Read the content of the response
    data = response.read()
    
    # Decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')
    
    # Print the HTML content of the web page
    print('HTML CONTENET '+html_content)

    file1 = open("extract.txt", "w")
    file1.writelines(html_content)
    file1.close()
except Exception as e:
    print("Error fetching URL:", e)
