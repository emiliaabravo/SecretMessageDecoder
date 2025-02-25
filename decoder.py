import requests
from bs4 import BeautifulSoup


def fetch_google_doc(url):
    """Fetch table data from a public Google Doc."""
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Failed to retrieve data.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")  # Locate the first table
    
    if not table:
        print("❌ No table found in the document.")
        return None

    rows = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cols = [col.text.strip() for col in row.find_all("td")]
        if len(cols) == 3:  # Ensure valid row structure
            rows.append(cols)
    
    return rows

def parse_text_to_grid(data):
    grid = {}

    # Skip header row
    for row in data[0:]:  # Skips the first line assuming it contains column headers
         # Split based on tab (may need adjusting)

        if len(row) != 3:
            print(f"Skipping invalid row: {row}")  # Debugging output
            continue  # Skip malformed rows

        x, char, y = row
        # Validate x and y before conversion
        if not x.isdigit() or not y.isdigit():
            print(f"Skipping non-numeric values: x={x}, y={y}")  # Debugging output
            continue

        grid[(int(x), int(y))] = char  # Store in dictionary

    return grid

def display_grid(grid):
    """
    Displays the extracted characters in a structured grid.
    - Finds min/max x and y values.
    - Fills empty spaces with " ".
    """
    if not grid:
        print("⚠️ No data to display.")
        return

    # Get grid boundaries
    min_x = min(x for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    # Generate and print grid
    for y in range(max_y, min_y - 1, -1):
        row = [grid.get((x, y), " ") for x in range(min_x, max_x + 1)]
        print("".join(row))  # Print row as a string

def main():
    url = input("🔗 Enter the Google Doc URL: ")
    data = fetch_google_doc(url)
    
    if data:
        grid = parse_text_to_grid(data)
        display_grid(grid)  # Print structured output

if __name__ == "__main__":
    main()