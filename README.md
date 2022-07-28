# Introduction

In this mini research, we are trying to see how media, in our case kompas.com, see conflict between MS Glow and PS Glow

# Tools

* Python 3.9
* BeautifulSoup
* Selenium
* Chrome Webdriver
* Google Chart

# Methodology

* Web scraping on Bing 
* Query used: kompas.com+ps+ms+glow

# Problems found with Bing Results

* Results are duplicated
* Some results are irrelevant

Here are our results after removing the duplicates and irrelevant search results:

```
Length before removing duplicates:  141
Length after removing duplicates:  34
Length before removing irrelevant results:  34
Length before removing irrelevant results:  18
```

# Codes

| Code               | Goal                                                                    |
|--------------------|-------------------------------------------------------------------------|
| msglow.py          | To extract title, date, url and news content                            |
| data_processing.py | To filter the results and export to JSON to be consumed by Google Chart |
| show.html          | HTML page to show timeline using Google Chart                           |

# Result

![image](https://github.com/arwankhoiruddin/msglow-psglow-text-analysis/raw/main/timeline.png)

This chart can be seen in live [here](https://sicss2.000webhostapp.com/): 

# Members

* Arwan Ahmad Khoiruddin
* Tiara Saputri Darlis
* Suatmi Murnani