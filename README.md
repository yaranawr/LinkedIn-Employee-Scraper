# LinkedIn Employee Scraper
A simple scraper for LinkedIn using Python and Selenium.
It captures employee names, descriptions, and profile links from a specified company and saves the data in a CSV file separated by semicolons.

You must be logged into LinkedIn using the default Chrome browser profile.
***
## Installation

Git clone this repository:

```
$ git clone https://github.com/yaranawr/LinkedIn-Employee-Scraper
$ cd LinkedIn-Employee-Scraper
$ python -m pip install -r requirements.txt
```

- [Download chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#stable).
## Usage

- Close all Chrome windows before running the script
- Copy the company "people" page link and paste it as an argument, as shown in the example below
- Do the same for the chromedriver path (e.g., "C:\Users\YOUR-USER\Downloads\chromedriver-win64\chromedriver.exe")

```
$ python linkedin_employee_scraper.py "https://www.linkedin.com/COMPANY/people/" "path/to/chromedriver"
```

After the scraping is completed, the employee information will be saved in a file named "linkedin_profiles.csv" in the same folder.
