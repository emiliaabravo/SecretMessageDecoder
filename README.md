# SecretMessageDecoder

This project is a **secret message decoder** that extracts table data from a Google Doc, processes it into a grid, and displays the hidden message using Unicode characters.

## 🔹 How It Works
1. Enter a **Google Docs link** containing a table with:
   - **x-coordinate** (X position)
   - **Character** (Unicode symbol)
   - **y-coordinate** (Y position)
2. The program fetches and organizes the data into a structured grid.
3. The message is displayed in the correct orientation.

## 🔹 Requirements
- **Python 3.x**
- Install dependencies:
  ```sh
  pip install requests beautifulsoup4

## 🔹 Usage

- python decoder.py

## 🔹 Test it

Try decoding with these sample links:
1. https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub

2. https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub


