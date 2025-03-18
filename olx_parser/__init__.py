from .arguments import args_parse
from .loader import get_page
from .parser import parse_page
from .save import save_to_csv, save_to_json


def main():
    # Parse arguments
    args = args_parse()

    site_parsed_data = []

    print(f"Scraping {args['url']}")

    for i in range(1, args["pages"] + 1):
        print(f"Scraping page {i}/{args['pages']}")
        # Request page from site
        page_content = get_page(args["url"], i)
        
        # Parse page and get taitle, price, date, location and url
        site_parsed_data += parse_page(page_content)
        
    if args["is_json"]:
        save_to_json(site_parsed_data, filename=args["filename"])
    else:
        save_to_csv(site_parsed_data, filename=args["filename"])
        
    print("Done")