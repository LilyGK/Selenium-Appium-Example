# MadColectiveTest


To been able to execute the tests, is needed to have clone the repository, and have installed the package in the `requirements.txt` files.

Specially pytest, selenium and appium.

Once they are installed this are the following steps to exectuce the code.
And move to the directory where are the tests you want to execute. 

## Web tests:
  
 `export LT_USERNAME ="lilia.96.k" export LT_ACCESS_KEY = "nAQb3fg1EFm9dBlEw6RVtjfWeiFl1wWsif7J2pDVWzCZ5rcXaQ"` 

 `pytest test_search_wikipedia_web.py -v`
 
## App tests: 
`export BS_USERNAME="liliakhabarova_LQBE2f" export BS_ACCESS_KEY="HkNnzbKz4EpijxnzN9d5"`

`pytest test_wikipedia_searching_app.py -v`

## All the tests:

Or just write both pair of credentials at the same time and execute all the tests in the proyect with this command:

`pytest -v`

### Reporting 
In both cases, we are executing the test in cloud, in the Web case, we are using lambdaTest and in the app case, Browserstack (the free version of LambdaTest don't support Mobile app testing) 

This providers supoort logs, screenshots, video recordings and in Lambdatest cases, analytics. (Screenshots and more info in Notion page) 

