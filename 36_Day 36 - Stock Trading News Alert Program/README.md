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
# Alpha Vantage
PRICE_API_KEY=...
PRICE_URL=https://www.alphavantage.co/query

# News API
NEWS_API_
NEWS_URL=https://newsapi.org/v2/everything?

# Email
TO_EMAIL=
PASSWORD=
HOST=smtp.gmail.com
FROM_EMAIL=

# Companies to track
COMPANIES=

# Price change threshold
PRICE_CHANGE_CONDITION=
```

    


