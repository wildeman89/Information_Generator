from bs4 import BeautifulSoup as BS
import requests, lxml

def main():
    decade_start = 1890
    decade_end = 2020
    # TESTING #
    # Checking to see if results are completing for each decade
    for decade in range(decade_start, decade_end, 10):
        print(f"Checking to see if results from {decade}'s")
        if decade >= 1900:
            continue
        site = get_site(decade)
        if site is None:
            print(f"{decade} was not found")
            continue
        print(f"{decade} was found")
        soup = soupify(site)
        site.close()
        headers = get_table_headers(soup)
        for header in headers:
            print(header.get_text(), end=" ")
        print()

# Functions
def get_site( decade ):
    """ This will take a decade, add it into the url, and get the site. """
    url = f"https://www.ssa.gov/oact/babynames/decades/names{decade}s.html"
    #### TEST ####
    # print(url)
    """ using the url to request the website """
    site = requests.get(url)
    if site.status_code == 200:
        return site
    return None

def soupify( site ):
    """ This function will use BeautifulSoup4 to pull the html from the site """
    return BS(site.text, "lxml")

def get_table_headers( soup ):
    """ This function will return a list of table headers from the table.
    Table header tags in html are <th>.
    """
    return soup.find_all("th")


# calling main
main()
