# LinkedIn Employee Scraper
A simple scraper for LinkedIn using Python and Selenium.
It captures employee names, descriptions, and profile links from a specified company and saves the data in a CSV file separated by semicolons.

You must be logged into LinkedIn using the default Chrome browser profile.

> LinkedIn updates its code frequently, so this script might require constant updates.
***
## Installation

Git clone this repository:

```
$ git clone https://github.com/yr4na/LinkedIn-Employee-Scraper
$ cd LinkedIn-Employee-Scraper
$ python -m pip install -r requirements.txt
```

There's no need to download chromedriver anymore, as the script now downloads it automatically.

## Usage

- **Close all Chrome browser windows before running the script**. If Chrome is open, the script will throw an error.
- Copy the company "people" page link and paste it as an argument, as shown in the example below

```
$ python linkedin_employee_scraper.py https://www.linkedin.com/COMPANY/people/
```

After the scraping is completed, the employee information will be saved in a file named "linkedin_profiles.csv" in the same folder.

## Output Example

```
https://linkedin.com/in/johndoe;John Doe;CEO at Doe Inc
https://linkedin.com/in/mary-2168521512;Mary Lee;Web Developer
...
```
