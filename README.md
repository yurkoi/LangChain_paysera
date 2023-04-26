### LongChain QA (OpenAI API) for search engine improvement

For test purposes, I checked your support's search engine https://support.paysera.com/index.php?/payseraeng/Knowledgebase/List (manually)
The search takes a long time, there are also irrelevant answers (see below).

Since I do not have access to data, I decided to try to create a search engine using BeautifulSoup for parsing information and LangChain QA
for indexing and extract information.

* first image from support search engine
* second one - LongChain QA 
1.
![My Image](pics/photo_1_2023-04-26_20-20-19.jpg)
![My Image](pics/photo_2_2023-04-26_20-20-19.jpg)
2.
![My Image](pics/photo_3_2023-04-26_20-20-19.jpg)
![My Image](pics/photo_4_2023-04-26_20-20-19.jpg)
3.
![My Image](pics/photo_5_2023-04-26_20-20-19.jpg)
![My Image](pics/photo_6_2023-04-26_20-20-19.jpg)

## Conclusions

The current implementation of the search engine on the site works, but there are some delays and some irrelevant answers in the top 5-7.
Using regular parsing with a combination of lang chain without access to data, you can create a search engine "on the knee" that will give more relevant answers