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
        ''' 
        Because of the way the table is, there are two headers above the
        main four headers needed: Males, Females.
        Will find an elogent way to deal with this, but for now, going to
        pop the first two columns and move on. Will save them in a variable
        incase they can be used later.
        '''
        _top_headers = [headers.pop(0), headers.pop(0)]
        rows = get_table_rows(soup)
        rows = clean_table_rows(rows)
        for row in rows:
            print(row)
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

def get_table_rows( soup ):
    """ This function will get the table rows. This should be the ranks of 
    the names, the names, and the number of people named with those names.
    The html tags for table rows: <tr>
    """
    return soup.find_all("tr")

def clean_table_rows( row_list ):
    ''' This function is going to take the rows from the table, and
    remove the unnecessary bits. The last row in the table is not needed,
    going to remove it. Should be identifiable by "colspan=4". Only td to
    have that attribute.
    '''
    clean_rows = []
    for row in row_list:
        temp_row = []
        for td in row.find_all("td"):
            if 'colspan' in td.attrs.keys():
                continue
            temp_row.append(td.get_text())
        if len(temp_row) > 1:
            clean_rows.append(temp_row)
    return clean_rows


# calling main
main()
