import pandas as pd
from pyhtml import html, head, body, table, tr, th, td, link, title

# Load Excel data
def load_transactions(file_path):
    return pd.read_excel(file_path)

# Generate HTML dashboard
def generate_dashboard(data):
    rows = [
        tr([td(cell) for cell in row])
        for row in data.values.tolist()
    ]
    return str(
        html(
            head(
                title("Bank Transactions Dashboard"),
                link(rel="stylesheet", href="../static/style.css")
            ),
            body(
                table(
                    tr([th(col) for col in data.columns]),
                    *rows
                )
            )
        )
    )

if __name__ == "__main__":
    # Load transactions
    transactions = load_transactions("../data/transactions.xlsx")
    
    # Generate HTML
    dashboard_html = generate_dashboard(transactions)
    
    # Save to file
    with open("templates/dashboard.html", "w") as f:
        f.write(dashboard_html)
    print("Dashboard generated: templates/dashboard.html")