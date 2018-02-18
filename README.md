# Wikipedia-Web-Crawler
Basic web crawler based upon the Udacity, [Introduction to Python Programming](https://eu.udacity.com/course/introduction-to-python--ud1110) course.

------------------------------------------------------------------------------------------------
Crawls Wikipedia by selecting the first link of each page. Crawls continuously until the Philosophy page is found, or the crawler navigates to a previously visited page.

Uses [requests](https://github.com/requests/requests) to get the html requests and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to navigate through a html response to find the first link.
