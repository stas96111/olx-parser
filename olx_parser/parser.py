from bs4 import BeautifulSoup

def parse_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    
    items_title_div = soup.find('div', {'data-cy': 'ad-card-title'})
    items_price_p = soup.find('p', {'data-testid': 'ad-price'})
    items_data_time_p = soup.find('p', {'data-testid': 'location-date'})
    
    output_data = []
    
    for item in items_title_div:
        title = item.text.strip()
        price = items_price_p.text
        
        # Split location and date
        location, date = items_data_time_p.text.split(' - ')
        
        url = item.find('a')['href']
        
        output_data.append((title, price, date, location, url))
        
    return output_data