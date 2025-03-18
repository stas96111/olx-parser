from bs4 import BeautifulSoup

base_url = "https://www.olx.ua"

def parse_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    
    items_title_div = soup.find_all('div', {'data-cy': 'ad-card-title'})
    
    output_data = []
    
    for item in items_title_div:
        price = item.find('p', {'data-testid': 'ad-price'}).text
        data_location = item.find_next('p', {'data-testid': 'location-date'})
        
        # Split location and date
        location, date = data_location.text.split(' - ')
        
        link = item.find('a')
        url = base_url + link['href']
        title = link.text
        
        output_data.append((title, price, date, location, url))
        
    return output_data