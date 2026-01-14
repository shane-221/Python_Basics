# Market News Alert System

### <u>Overview</u> 
The Market News Alert System monitors key financial indicators using the AlphaVantage API and detects significant price movements.
When a price crosses a predefined threshold, the system automatically retrieves relevant news articles and sends a structured email alert summarising the event. 
This allows users to stay informed about market‑moving developments in real time.

### <u>Who is it for?</u>
- Indicvidual investors: Tracking certain stocks and want to check why there is a price movement without manually checking the news. 
- Traders : Traders who requres fast information to make decisions 
- Financial analysts/ Economic Analyst: Inidivuals who monitor multiple variables and need a lightweight system to sruface relanat news. 
- Anyone who wants automated email alerts.

### <u>Demo</u> 
[Video of Terminal outputs](./Multimedia/Output%20files.mp4)\
[Email Output](./Multimedia/Output_email.jpg)
* Please note: Can apply these outputs for multiple companies in the same format. 


### <u>Please Note</u>
- Rate limit is handled using a 0.5 second pause using the ``` time.sleep()````function. 
- Currently the errors are separated using if/elif/else statements and printed into the terminal. 
- 
### <u>Installation</u>

Follow these steps to set up the Market Alert System on your machine:
1) Clone the repository: 
```bash 
git clone {Name of the repostory I create}.git
cd repository
```

2) Create a virtual environment 

```
# Create the .venv file ( Powershell)

python -m venv .venv 

# Activate the file 
.venv\Scripts\activate
```
3) Create a .env file in the Confidential_Data directory
4) State these parameters within the .env file: 
```
-------------------------------------------------------------------------------------------------
                                        # Alpha Vantage
-------------------------------------------------------------------------------------------------
PRICE_API_KEY=                                          
        ## Go to Alphavantage and get an API Key
PRICE_URL=https://www.alphavantage.co/query

-------------------------------------------------------------------------------------------------
                                        # News API
-----------------------------------------------------------------------------------------------
NEWS_API_=                                               
        ## Go to News API and get an API Key
NEWS_URL=https://newsapi.org/v2/everything?

-------------------------------------------------------------------------------------------------
                                        # Email
------------------------------------------------------------------------------------------------
TO_EMAIL=
PASSWORD=
HOST=smtp.gmail.com                                     
        ## This is the SMTP host from where the email will be sent
FROM_EMAIL=

-------------------------------------------------------------------------------------------------
                                        # Companies to track
-------------------------------------------------------------------------------------------------
COMPANIES=                                              
        ## Run the list_of_stocks_apii from Comapnies_List. This pulls the most recent active companies 
        ## Place the ticker of the company into this section separated with commas. 

-------------------------------------------------------------------------------------------------
                                    # Price change threshold
-------------------------------------------------------------------------------------------------

PRICE_CHANGE_CONDITION=                                
        ## This will be the parameter that  triggers whether there is a significant change in the value of interest. 
```
5. Add these files to the to the `gitignore` file: 
```
Confidential_data_file/.env
.venv
```
6. Run `main.py` to start the program from the file `Main_Code`.


### <u>Folder Structure </u>
 ```
Market_Alert_System/
│
├── .idea/                      # [IDE config files — add notes if needed]
│   
│
├── .venv/                      # [Python virtual environment — dependencies installed here]
│
├── Companies_List/             # [Company tickers and API script]
│   │
│   ├── Companies_list.csv              ## [CSV of active companies]
│   └── list_of_stocks_api.py           ## [Script to pull tickers from external API]
│
├── Confidential_data/         # [Sensitive credentials stored here]
│   │
│   └── .env                            ## [Environment variables: API keys, email credentials, etc.]
│
├── Documentation/             # [Setup notes and instructions]
│   │
│   └── Steps.txt                       ## [Manual steps or installation guide]
│
├── Main_Code/                 # [Core logic for running the alert system]
│   │
│   ├── __pycache__/           
│   └── main.py                         ## [Main script that runs the alert system]
│
├── Multimedia/                # [Demo outputs]
│   │
│   ├── Output files.mp4                ## [Video showing terminal output]
│   └── Output_email.jpg                ## [Screenshot of email alert]
│
├── Output_Emails/             # [Sample email outputs]
│   │
│   ├── output_format_2026-01-04.html
│   ├── output_format_2026-01-05.html
│   ├── output_format_2026-01-06.html
│   └── output_format_2026-01-08.html
│
├── Structures/                # [Functionalities of Main.py broken into classes.]
│   │
│   ├── __pycache__/           
│   ├── email_format.html               ## [HTML template for email alerts]
│   ├── news_request_api.py             ## [Fetches news articles from News API]
│   ├── send_email.py                   ## [Handles email sending via SMTP]
│   ├── stock_request_api.py            ## [Fetches stock price data from AlphaVantage]
│   └── website_code_conversion.py      ## [Cleans and formats scraped website content]
│
├── .gitignore                 # [Specifies files/folders Git should ignore]
└── README.md                  # [Project documentation]

```

