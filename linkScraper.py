import requests
from bs4 import BeautifulSoup

def scrape_all_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Find all <a> elements with an 'href' attribute
        anchors = soup.find_all('a', href=True)

        # Filter links that start with "/"
        links.extend([anchor['href'] for anchor in anchors if anchor['href'].startswith("/")])

        return links
    else:
        print(f"Failed to fetch page: {url}")
        return []

def save_links_to_file(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(f"\"https://www.whatmobile.com.pk{link}\",\n")

if __name__ == "__main__":
    main_page_url = "https://www.whatmobile.com.pk/0_to_150001_Mobiles"
    all_links = scrape_all_links(main_page_url)

    if all_links:
        save_links_to_file(all_links, "links.txt")
        print(f"Filtered links saved to 'links.txt'")
