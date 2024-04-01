#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Essential webscrap imports
import requests
from bs4 import BeautifulSoup
import re
from lxml import html

#VIsualization and data frame setup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#url list for ease of iteration for Energy Companies (Exxon Mobil, Chevron, Shell)
urls = ["https://www.alphaspread.com/security/nyse/xom/financials/cash-flow-statement/free-cash-flow",
        "https://www.alphaspread.com/security/nyse/cvx/financials/cash-flow-statement/free-cash-flow",
        "https://www.alphaspread.com/security/lse/shel/financials/cash-flow-statement/free-cash-flow"]

for u in urls:
    #Sending a GET request to the URL and storing the response
    response = requests.get(u)

    #Checking to see if it was successful
    if response.status_code == 200:
        #Using BeautifulSoup to parse data
        soup = BeautifulSoup(response.content, "html.parser")
    else:
        #Unsuccessful case
        print("Failed", response.status_code)

    #HTML content paragraph tags
    paragraphs = soup.find_all("p")

    #Loop through each paragraph found
    for paragraph in paragraphs:
        #Extracting text
        text = paragraph.text
        match = re.search(r'(\d+(?:\.\d+)?)([BM])\sUSD', text)
        if match:
            #Extracting the value & its unit
            value_str, unit = match.groups()
            #Conversion 
            value = float(value_str)
            #Scaling 
            if unit == 'B':
                value *= 1e9 #Billion to int
                value = int(value) 
            elif unit == 'M':
                value *= 1e6  #Million to int
                value = int(value)
            print(value)


# In[4]:


#FCF extracting for our dataframe (similar steps to previous iteration of FCF output)
def extract_free_cash_flow(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            text = paragraph.text
            #Using regular expression search method to be specific
            match = re.search(r'Based on the financial report.*?amounts to (\d+(?:\.\d+)?)([BM])\sUSD', text)
            if match:
                value_str, unit = match.groups()
                value = float(value_str)
                if unit == 'B':
                    value *= 1e9  
                    value = int(value)  
                elif unit == 'M':
                    value *= 1e6 
                    value = int(value)  
                return value
    else:
        print("Failed to retrieve page:", response.status_code)

urls = [
    "https://www.alphaspread.com/security/nyse/xom/financials/cash-flow-statement/free-cash-flow",
    "https://www.alphaspread.com/security/nyse/cvx/financials/cash-flow-statement/free-cash-flow",
    "https://www.alphaspread.com/security/lse/shel/financials/cash-flow-statement/free-cash-flow",
]

#Iterating through our list
companies = ["Exxon Mobil", "Chevron", "Shell"]
free_cash_flows = [extract_free_cash_flow(url) for url in urls]

#Creating our dataframe
df = pd.DataFrame({
    "Company": companies,
    "Free Cash Flow": free_cash_flows
})

#Visualization setup
sns.set_style("whitegrid")

#Tailoring our visualization with color changes
plt.figure(figsize=(10, 6))
sns.barplot(x='Company', y='Free Cash Flow', data=df, palette='viridis')
plt.title('Free Cash Flow of Companies')
plt.xlabel('Company')
plt.ylabel('Free Cash Flow (USD)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()


# In[5]:


df


# In[6]:


#Similar to before 
url = "https://www.alphaspread.com/security/nyse/xom/relative-valuation"
response = requests.get(url)

if response.status_code == 200:
    #Parsing the HTML content with lxml
    tree = html.fromstring(response.content)
    
    #Using XPath to extract our first P/S ratio
    ps_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[0]
    
    #Identical for P/E ratio
    pe_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[1]
    
    print("P/S Ratio:", ps_ratio_element)
    print("P/E Ratio:", pe_ratio_element)
else:
    #In case it is unresponsive
    print("Failed")


# In[7]:


#Identical to above
url = "https://www.alphaspread.com/security/nyse/cvx/relative-valuation"
response = requests.get(url)
if response.status_code == 200:
    #Parsing
    tree = html.fromstring(response.content)
    
    #Extracting for both ratios
    ps_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[0]
    pe_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[1]
    
    print("P/S Ratio:", ps_ratio_element)
    print("P/E Ratio:", pe_ratio_element)
else:
    print("Failed")


# In[8]:


url = "https://www.alphaspread.com/security/lse/shel/relative-valuation"
response = requests.get(url)

if response.status_code == 200:
    tree = html.fromstring(response.content)
    ps_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[0]
    pe_ratio_element = tree.xpath('//div[@class="weight-700 left-aligned value color-blue-400"]/text()')[1]
    
    print("P/S Ratio:", ps_ratio_element)
    print("P/E Ratio:", pe_ratio_element)
else:
    print("Failed")


# In[ ]:




