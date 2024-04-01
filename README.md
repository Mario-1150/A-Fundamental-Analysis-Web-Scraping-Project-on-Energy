# A Fundamental Analysis Web Scraping Project with Python
## Energy Company Analysis
This project is designed to perform financial analysis on three major energy companies: Exxon Mobil, Chevron, and Shell. It utilizes web scraping techniques to extract financial data from the companies' websites, analyzes their free cash flows, and visualizes the data using Python libraries such as BeautifulSoup, Pandas, Seaborn, and Matplotlib.

## Introduction
Financial analysis is crucial for understanding the performance and health of companies. This project aims to provide insights into the financial standing of Exxon Mobil, Chevron, and Shell by analyzing their free cash flow, a key metric indicating a company's ability to generate cash after accounting for expenses. Additionally, it extracts relative valuation metrics such as Price-to-Sales (P/S) and Price-to-Earnings (P/E) ratios to evaluate the companies' market valuation.

## Installation
Installing the following Python Libraries serves as a prerequisite
**requests** for sending HTTP requests to fetch web pages
**lxml** for parsing XLM content
**pandas** for data amnipulation & analysis
**beautifulsoup4** for parsing HTML content
**seaborn** for statistical data visualization
**matplotlib** for creating static, animated, and interactive visualizations in Python

## Summary of Steps
This script performs the following steps:

- Sends HTTP requests to the URLs of the cash flow statements of Exxon Mobil, Chevron, and Shell.

- Parses the HTML content of the web pages using BeautifulSoup.

- Extracts free cash flow data from the financial statements.

- Creates a DataFrame using Pandas to store the extracted data.

- Visualizes the free cash flow data using Seaborn and Matplotlib.

- Extracts relative valuation metrics (P/S and P/E ratios) from the companies' websites.

- Prints the extracted metrics for each company.

## Features & Notes
- Scrapes free cash flow data from energy companies' financial statements.

- Visualizes free cash flow data using Seaborn and Matplotlib.

- Extracts relative valuation metrics (P/S and P/E ratios) from company websites.

- Provides insights into the financial performance of energy companies.

## Relative Valuation
The project extracts and displays the Price-to-Sales (P/S) and Price-to-Earnings (P/E) ratios for each company. These metrics are important for evaluating the market valuation of companies and comparing them with industry peers.
For more information on Free Cash Flow, Price to Earnings and Price to Sales see the links below
https://en.wikipedia.org/wiki/Free_cash_flow
https://en.wikipedia.org/wiki/Price%E2%80%93earnings_ratio
https://en.wikipedia.org/wiki/Price%E2%80%93sales_ratio

