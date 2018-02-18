# Wikipedia-Web-Crawler
Basic web crawler inspired by the Udacity, [Introduction to Python Programming](https://eu.udacity.com/course/introduction-to-python--ud1110) course.

------------------------------------------------------------------------------------------------
Crawls Wikipedia by selecting the first link of each page. Crawls continuously until the specified page is found, or the crawler navigates to a previously visited page.

## Arguments
'-s [URL]' - Specifies a start URL. If not provided, defaults to a random wikipedea page  
'-g [URL]' - Specifices a goal URL. If not provided, defaults to https://en.wikipedia.org/wiki/Philosophy

## Requirements
[Requests](https://github.com/requests/requests)  
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

