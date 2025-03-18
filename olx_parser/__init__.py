from arguments import args_parse
from loader import get_page
from parser import parse_page

# Parse arguments
args = args_parse()

site_parsed_data = []

for i in range(1, args["pages"] + 1):
    # Request page from site
    page_content = get_page(args["url"], i)
    
    # Parse page and get taitle, price, date, location and url
    site_parsed_data += parse_page(page_content)
    
print(site_parsed_data)