<div align="center">
  <a href="http://kay.ai">
    <img src="https://i.ibb.co/7jT6nnL/photo-2023-08-30-10-05-04.jpg" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">kay</h3>

  <p align="center">
    Data API for Context Retrieval <br/>
   🚀 <a href="https://kay.ai"><strong>Recent Company Data Embeddings »</strong></a>
 
  </p>
  <a href="https://pepy.tech/project/embedstore" alt="Downloads">
        <img src="https://static.pepy.tech/personalized-badge/embedstore?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/month" /></a>
  <a>
    <img src="https://img.shields.io/github/license/embeddingstore/embedstore"/>
  </a>
  <p align="center">
    <br />
     <a href="https://colab.research.google.com/drive/1yhBhLmiPNtc06qVnjQRLsWuQDID3_cwl?usp=sharing">Try on Google Colab</a>
    ∙
    <a href="https://playground.embedding.store/podcasts?__theme=light">Test API</a>
    ∙
    <a href="https://www.embedding.store/">Subscribe for Early Access</a>
  </p>
</div>


## Quick start
### Installation
You have two ways to get started:
1. Install our python library : `pip install kay`
2. Directly call the endpoint : `https://api.kay.ai/retrieve`


### Get API Key [here](https://api.kay.ai/register)
**Note:** Currently we are rate-limiting all API keys to 100 requests/day

Set the `KAY_API_KEY` as environment variable
```python
import os
os.environ["KAY_API_KEY"] = <YOUR API KEY> 
```
Pass the API key as header if you are calling the endpoint directly. More details about the [endpoint](#using-retrieve-endpoint)
```python
headers = {'API-Key': <YOUR_API_KEY>}
```

### Retrieve context
In a few lines of code, you can now start retrieving relevant context to get better answers from your LLM. We are starting with indexing all company related data inclucing SEC filings, Press release and more. 
```python
from kay.rag.retrievers import KayRetriever

# Initialize the retriever
retriever = KayRetriever(dataset_id = "company",  data_sources=["10-K", "10-Q", "8-K", "PressRelease"])

# Query the retriever
context = retriever.query(query="What is the state of the art in Autonomous Driving security and safety?",num_context=3)

# Examine the retrieved context and then append it to the prompt before you call your LLM
print(context[0])
```

Read more [here](#usage) for detailed usage guidelines. 

## What is this?
We are building context retrieval apis for developers to connect their LLMs to global data with fully hosted embeddings.

Read more about RAG (retrieval augmented generation) [here](https://twitter.com/pwang_szn/status/1663123050097946624). 

<img src="https://i.ibb.co/hR07N8k/content.png" alt="Logo">

## Usage
### More about `KayRetriever` class
`KayRetriever` serves as the single point of entrance to interact with the Kay.

Parameters to initialize the class :
- `dataset_id (str)` : (Required) Dataset to query and retrieve context from (eg: `company`)
- `data_sources (int)` : (Optional) List of data sources you want us to search on. You can leave it empty and we will figure out the best context given your query.


### Retrieving contexts based on query
You can use `KayRetriever.query()` to get context based on the user prompt.

The `query()` function takes three inputs:
- `query (str)`: (Required) The user prompt that you are querying for 
- `num_context (int)`: (Optional) Number of context you want to fetch. Default = 6
- `instruction (str)`: (Optional) Specific instructions to the retriever in natural language (eg: "Be more generic and broad", "Retrieve specific numbers", etc.).

#### Example:  TBD

```python

```


### Using `/retrieve` endpoint 
**Sample code**
  ```python
  import requests
  url = 'https://api.kay.ai/retrieve'
  headers = {'API-Key': <YOUR_API_KEY>}

  # creating the payload
  payload = {"query": <PROMPT>,"dataset_config": {"dataset_id":"company", "data_sources":["10-K", "10-Q", "8-K", "PressRelease"]},"retrieval_config:{"num_context":6}}

  response = requests.post(url, headers=headers,payload=payload)

  # check the response
  print(response.json())
  ```

**Authorization**
Add the API key in the header : `{'API-Key'='<YOUR_API_KEY>'`

**Parameters**
| Param             | Details | Type  | Example
| ------------------- | ----------------------------- | -------- | ----------------------------- |
| query | the prompt on which context need to be retrieved  | `str`  | `What does Tim Ferris say about productivity?` |
| dataset_config | a dictionary of dataset specific parameters like dataset_id and data_sources.  |  `dict` | `{"dataset_id":"company", "data_sources":["10-K", "10-Q", "8-K", "PressRelease"]}` |
| retrieval_config | a dictionary of retrieval specific parameters like num_context and instruction. |  `dict` | `{"num_context":6}` |


By default, the API returns the top 6 contexts right now. We will be adding options to control this soon.

**Sample Response**
```json
{
    "contexts": [
        {
            "_additional": {
                "id": "3be8769e-a0fb-4741-845b-b0dcaaeed839"
            },
            "chunk_embed_text": "Company Name: CAMPBELL SOUP CO \n Company Industry: FOOD AND KINDRED PRODUCTS \n Form Title: 10-Q 2023-Q1 \n Form Section: Risk Factors \n Text: The ultimate impact depends on the severity and duration of the pandemic, including the emergence and spread of new COVID 19 variants and resurgences, the continued availability and effectiveness of vaccines and actions taken by government authorities and other third parties in response to the pandemic.We will continue to evaluate the extent to which the COVID 19 pandemic will impact our business, consolidated results of operations and financial condition.Net periodic pension and postretirement benefit income excluding any actuarial losses or gains is estimated to be approximately $35 million lower in 2023, subject to the impact of interim remeasurements.The decrease in 2023 is due to increases in discount rates used to determine the benefit obligations and a decline in the market value of plan assets.Summary of Results This Summary of Results provides significant highlights from the discussion and analysis that follows.Net sales increased 15% in the quarter to $2.575 billion due to inflation driven pricing and sales allowances, partially offset by volume declines.Gross profit, as a percent of sales, was 32.4% in 2023 compared to 32.3% in the prior year quarter.The increase was primarily due to inflation driven pricing actions, supply chain productivity improvements, lower promotional spending and lower restructuring related costs, partially offset by higher cost inflation and other supply chain costs as well as unfavorable volume/mix.",
            "chunk_type": "text",
            "chunk_years_mentioned": [
                2023
            ],
            "company_name": "CAMPBELL SOUP CO",
            "company_sic_code_description": "FOOD AND KINDRED PRODUCTS",
            "data_source": "10-Q",
            "data_source_link": "https://www.sec.gov/Archives/edgar/data/16732/000001673222000156",
            "data_source_publish_date": "2023-01-01T00:00:00Z",
            "data_source_uid": "0000016732-22-000156",
            "title": "CAMPBELL SOUP CO |  10-Q 2023-Q1 "
        },
        {
            "_additional": {
                "id": "aa417ac9-2da0-48a5-9c9d-2a8b5a7d55f3"
            },
            "chunk_embed_text": "Company Name: NIGHTFOOD HOLDINGS INC \n Company Industry: SUGAR & CONFECTIONERY PRODUCTS \n Form Title: 10-Q 2023-Q1 \n Form Section: Financial Statements \n Text: The accompanying financial statements do not include any adjustments to reflect the possible future effects on recoverability and reclassification of assets or the amounts and classification of liabilities that may result from the outcome of this uncertainty.The outbreak of the novel coronavirus (COVID 19), including the measures to reduce its spread, and the impact on the economy, cannot fully be understood and identified.Indications to date are that there are somewhat offsetting factors relating to the impact on our Company.Industry data shows that supermarket sales remain up, with more people spending more time at home.Anecdotally and statistically, snacking activity is also up while consumers are reporting a decrease in sleep quality and sleep satisfaction.The offsetting factors are the impact of the virus on the overall economy, and the impact that a down economic period can have on consumer behavior, including potential reductions in travel, hotel occupancy, and trial of new brands.Greater unemployment, recession, and other possible unforeseen factors are shown to have an impact.Research indicates that consumers are less likely to try new brands during economic recession and stress, returning to the legacy brands they've known for decades.",
            "chunk_type": "text",
            "chunk_years_mentioned": [],
            "company_name": "NIGHTFOOD HOLDINGS INC",
            "company_sic_code_description": "SUGAR & CONFECTIONERY PRODUCTS",
            "data_source": "10-Q",
            "data_source_link": "https://www.sec.gov/Archives/edgar/data/1593001/000121390022074226",
            "data_source_publish_date": "2023-01-01T00:00:00Z",
            "data_source_uid": "0001213900-22-074226",
            "title": "NIGHTFOOD HOLDINGS INC |  10-Q 2023-Q1 "
        },
        {
            "_additional": {
                "id": "9dec26c4-6f3b-482f-be9c-f4bacd8f0f09"
            },
            "chunk_embed_text": "Company Name: BEYOND MEAT INC \n Company Industry: FOOD AND KINDRED PRODUCTS \n Form Title: 10-K 2022-FY \n Form Section: Risk Factors \n Text: Starting in 2020, the COVID 19 pandemic had a significant impact on the worldwide economy and, in turn, our business, financial condition and results of operations.Although we expect the impacts of the pandemic, and the resulting effects on the economy, on us to continue to decline, we are likely to see certain prolonged effects.For example, certain of our QSR customers reduced their menu offerings in response to COVID 19, which negatively impacted plant based food items.If those customers are slow to re expand their menus, or choose not to put plant based products back on their menus, our business could be adversely affected.As global economic conditions continue to be volatile or uncertain and recessionary or inflationary pressures exist, trends in consumer discretionary spending also remain unpredictable and subject to changes.We have seen consumers shift purchases to lower priced or other perceived value offerings during economic downturns as a result of various factors, including job losses, inflation, higher taxes, reduced access to credit, change in federal economic policy and recent international trade disputes.In particular, consumers have reduced the amount of plant based food products that they purchase where there are conventional animal based protein offerings, which generally have lower retail prices.In addition, consumers may choose to purchase private label products rather than branded products because they are generally less expensive.",
            "chunk_type": "text",
            "chunk_years_mentioned": [
                2020
            ],
            "company_name": "BEYOND MEAT INC",
            "company_sic_code_description": "FOOD AND KINDRED PRODUCTS",
            "data_source": "10-K",
            "data_source_link": "https://www.sec.gov/Archives/edgar/data/1655210/000165521023000017",
            "data_source_publish_date": "2022-01-01T00:00:00Z",
            "data_source_uid": "0001655210-23-000017",
            "title": "BEYOND MEAT INC |  10-K 2022-FY "
        }
    ],
    "success": "true"
}

```
