import csv, json


def file_ending(filename, ending):
    if not filename.endswith(ending):
        return f"{filename}{ending}"


def save_to_csv(data, filename = "output.csv"):
    filename = file_ending(filename, ".csv")
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(('Title', 'Price', 'Date', 'Location', 'Url'))
        writer.writerows(data)
    
    
def save_to_json(data, filename = "output.json"):
    filename = file_ending(filename, ".json")
    # Add keys to data
    data = [dict(zip(["title", "price", "date", "location", "url"], data_tuple)) for data_tuple in data]
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)