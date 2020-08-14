---
title: Data Crawling with Scrapy
description: Small project of data crawling.
categories:
  - web
#cover: '/assets/images/intro_api/api.png'
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Scrapy / Web / Data Crawling
#header:
#  image: /assets/images/logos/logo-text-8c3ba8a6.svg
---
# What is Scrapy
Scrapy can be used for 1) extracting the data from websites and 2) saving them in your preferred format. In general, data crawling can be done easily if collecting data is small. However, as your data size gets bigger, number of URLs and that of crawler source codes become complicated to maintain. Scrapy solves the challenges that come from the issue mentioned above.
- modularized with spider, item, pipeline, selector, etc. so that unnecessary reusable programming (called "boilerplate code") is not required.
- If data size is big, process of data crawling gets slower. To make the process faster, async (asynchronous) operating like Parallel Thread in Python can be used. Scrapy can work asynchronously.

## Scrapy Architecture

Fig1 shows the created project directory. I commanded `$ scpary startproject companycrawler` in the terminal.

![scrapy_archit](/assets/images/Data-Crawling-Scrapy/scrapy_archit.png){:height="800px" width="400px"}  
| Fig1. Scrapy Project Directory |

  companycrawler/          # project's Python module, you'll import your code from here
    __init__.py

    items.py          # project items defined (a class with attributes) to provide functionalities.

    middlewares.py    # project communicator between the Engine and the Spiders that process spider input (responses) and output (items and request).

    pipelines.py      # project pipelines that process the extracted items like cleansing, validating, and persistent storing. Think of it as a passage for storing items.  

    settings.py       # project settings file

    spiders/          # a directory where you'll later put your spiders of cutomized classes.
        __init__.py
        ...

  scrapy.cfg            # deploy configuration file

Let me connect the these files and directories to the Scrapy architecture diagram shown below.

![scrapy_archit_all](/assets/images/Data-Crawling-Scrapy/scrapy_archit_all.png){:height="800px" width="600px"}  
| Fig2. Scrapy Architecture Diagram |

1. The Engine gets the initial Requests to crawl from the Spider which is customized classes by users to parse responses and extract items. It can work asynchronously.
2. The Engine schedules the Requests in the Scheduler and gets ready for the next Requests from it.
3. The Scheduler returns the next Requests to the Engine.
4. The Engine sends the Requests to the Downloader through the Downloader Middlewares.
5. The Downloader sends the Response, after done with downloading, to the Engine.
6. The Engine sends the Response from the Downloader to the Spider for processing.
7. The Spider processes the Response and returns scraped items and new Requests to the Engine.
8. The Engine sends processed items to the Pipelines and processed Requests to the Scheduler.

These steps can be repeated until there is no more requests from the Scheduler.

## Project (Scrawling the job data)
