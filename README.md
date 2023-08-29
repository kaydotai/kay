<div align="center">
<!--   <a href="http://kay.ai">
    <img src="https://i.ibb.co/x5TTmQC/64ea2e977e148519763205e7-logo-test.png" alt="Logo" width="167" height="47">
  </a> -->

  <h3 align="center">kay</h3>

  <p align="center">
    Context retrieval apis to power your LLMs! <br/>
   🚀 <a href="https://playground.embedding.store/wikipedia/?__theme=light"><strong>Recent Wikipedia embeddings launch »</strong></a>
 
  </p>
  <a href="https://pepy.tech/project/embedstore" alt="Downloads">
        <img src="https://static.pepy.tech/personalized-badge/embedstore?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/month" /></a>
  <a href="https://discord.com/invite/hAnE4e5T6M">
    <img src="https://img.shields.io/discord/1111412701651013713?label=discord" />
  </a>
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
We are building context retrieval apis for developers creating chatbots, copilots and search tools on top of LLMs. You no longer need to maintain scraping and embedding pipelines, and instead focus on building your product. 

Read more about RAG (retrieval augmented generation) [here](https://twitter.com/pwang_szn/status/1663123050097946624). 

<img src="https://i.ibb.co/jgQc4z9/Mindmap.png" alt="Logo">

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

#### Example 1:  TBD

```python

```

#### Example 2:  TBD

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
TBD
```json

```

## Datasets
TBD

## Get involved
TBD
