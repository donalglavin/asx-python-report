# Introduction.
The objective of this repository is to complete a financial assessment and summary of the Australian Stock Exchange EOD every week day. 
The output will consist of a daily report of the current general market trends, industry tends and overall highest and lowest performers

This is currently a work in progress and a rudamentary approach to webscraping, financial analysis web-development and github actions to automate 
reporting and analysis of financial markets. 
The future goal will be to have the output update an insteractive SPA webapp hosted on github pages 
(as this commit it will simply be included in the github README) as well as providing a basic endpoint for others to access the data.

This is my first attempt at completing something like this so expect a lot of change in the contents, srtategy and outputs of this repo moving forward.

If you are interested, you can can subscribe to watch this project and get notified each time there is a commit.
This will send you an email either when I update a feature or when the github action updates the report/SPA.

## Disclaimer. 
*All information contained within this repository is for educational purposes only,
I am not licensed to provide financial advice and take no responsibility for any action you take as a result
of the information contained within in this resource.*

# Roadmap. 
The current roadmap/plan is as follows:
1. Configure a basic github actions file that will run everyday at **4:00pm** Sydney time to align with the market close of the ASX trading period.
2. Develop a script (using freely available data only) to retrieve the financial market information for all publicly listed companies on the ASX. 
3. Complete the following assessment: 
  - A general overview of the market trends.
  - Provide a inter-industry level assessment for industry specific performance relative to other industries.
  - Provide an intra-industry level assessment for companies within each industry.
  - Provide a general stock assessment for individual stocks.
  - Assess indexes and etfs based on exposure to individual stocks and industies (TBA).
4. Develop as SPA app to be hosted on github pages to allow people to view and query the assessments. 

# Methodology. 
The current approach (subject to change) is to query the ASX financial data contained within the official ASX 
website and other freely available sources to summarised overall market value and percentage change of 
shares at the end of every weekday. 

Setting up a system like this allows for transparent changes in history (by going through historic commits) as well as 
providing a esasily accessible and up to date resource for financial data.

# Results.
*Once sufficient a link to the Reports.md File will be added below.*
