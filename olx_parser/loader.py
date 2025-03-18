import requests


def get_page(url: str, page_number = 1) -> str:
    url = f"{url}?page={page_number}"
    
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")    
    
    return response.text