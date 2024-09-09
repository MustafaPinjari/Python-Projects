import os
import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from twilio.rest import Client as TwilioClient

# Twilio WhatsApp setup (Replace these with your Twilio credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio Sandbox WhatsApp number

# Function to create the PDF invoice
def create_invoice_pdf(company_name, company_address, company_city, products, total, message, file_name):
    # Ensure the Downloads directory exists
    downloads_dir = os.path.join(os.getcwd(), 'Downloads')
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
    
    # Create the full path for the PDF file
    pdf_file = os.path.join(downloads_dir, f"{file_name}.pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Add a logo image to the top right corner
    logo_path = "Images/VadaPav.png"  # Path to your logo file
    if os.path.exists(logo_path):
        c.drawImage(logo_path, width - 100, height - 180, width=80, height=80)  # Adjusted position
    
    # Top border
    c.drawString(30, height - 30, '---' * 50)

    # Company information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 60, f"{company_name.title()}")
    c.drawString(40, height - 80, f"{company_address.title()}")
    c.drawString(40, height - 100, f"{company_city.title()}")

    # Line between sections
    c.drawString(30, height - 120, '---' * 50)

    # Header for section of items
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height - 140, "Product Name")
    c.drawString(250, height - 140, "Quantity")
    c.drawString(400, height - 140, "Product Price")

    # Print statement for each item
    c.setFont("Helvetica", 10)
    y_position = height - 160
    for product in products:
        c.drawString(30, y_position, product['name'].title())
        c.drawString(250, y_position, str(product['quantity']))
        c.drawString(400, y_position, f"₹{product['total_price']:.2f}")
        y_position -= 20

    # Line between sections
    c.drawString(30, y_position - 10, '---' * 50)

    # Header for section of total
    y_position -= 30
    c.setFont("Helvetica-Bold", 10)
    c.drawString(400, y_position, "Total")

    # Calculate and print total price
    c.setFont("Helvetica", 10)
    y_position -= 20
    c.drawString(400, y_position, f"₹{total:.2f}")

    # Line between sections
    y_position -= 10
    c.drawString(30, y_position, '---' * 50)

    # Output thank you message
    y_position -= 30
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(30, y_position, message)

    # Bottom border
    y_position -= 20
    c.drawString(30, y_position, '*' * 50)

    # Developer credits
    y_position -= 40
    c.setFont("Helvetica", 8)
    c.drawString(30, y_position, "Developed by Mustafa Pinjari")

    # Add clickable links
    y_position -= 15
    c.setFillColorRGB(0, 0, 1)  # Set color to blue for link
    c.drawString(30, y_position, "GitHub")
    c.linkURL("https://github.com/MustafaPinjari", (30, y_position, 80, y_position + 10))

    y_position -= 15
    c.drawString(30, y_position, "LinkedIn")
    c.linkURL("https://www.linkedin.com/in/mustafa-pinjari-287625256/", (30, y_position, 80, y_position + 10))

    c.save()
    messagebox.showinfo("Success", f"Invoice saved as {pdf_file}")

    # Send PDF via WhatsApp
    send_whatsapp_message(client_number, pdf_file)

# Function to send the PDF via WhatsApp
def send_whatsapp_message(client_number, pdf_file):
    client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Here is your invoice.",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=f'whatsapp:{client_number}',
        media_url=f'https://your-server.com/path-to/{os.path.basename(pdf_file)}'
    )
    messagebox.showinfo("Success", f"Invoice sent to {client_number}")

# Function to handle the form submission
def submit_form():
    company_name = entry_company_name.get()
    company_address = entry_company_address.get()
    company_city = entry_company_city.get()
    file_name = entry_file_name.get()
    client_number = entry_client_number.get()
    message = 'Thanks for shopping with us today!'

    total = sum(product['total_price'] for product in products)
    create_invoice_pdf(company_name, company_address, company_city, products, total, message, file_name)

# Function to add a new product to the list
def add_product():
    product_name = entry_product_name.get()
    product_price = float(entry_product_price.get())
    quantity = int(entry_product_quantity.get())
    total_price = product_price * quantity
    products.append({'name': product_name, 'price': product_price, 'quantity': quantity, 'total_price': total_price})
    listbox_products.insert(tk.END, f"{product_name} - Qty: {quantity} - ₹{total_price:.2f}")
    entry_product_name.delete(0, tk.END)
    entry_product_price.delete(0, tk.END)
    entry_product_quantity.delete(0, tk.END)
    entry_product_name.focus()

# Function to move focus to the next entry widget
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Initialize the main window
root = tk.Tk()
root.title("Invoice Generator")
products = []

# Company information fields
ttk.Label(root, text="Company Name:").grid(row=0, column=0, padx=10, pady=5)
entry_company_name = ttk.Entry(root)
entry_company_name.grid(row=0, column=1, padx=10, pady=5)
entry_company_name.bind("<Return>", focus_next_widget)

ttk.Label(root, text="Company Address:").grid(row=1, column=0, padx=10, pady=5)
entry_company_address = ttk.Entry(root)
entry_company_address.grid(row=1, column=1, padx=10, pady=5)
entry_company_address.bind("<Return>", focus_next_widget)

ttk.Label(root, text="Company City:").grid(row=2, column=0, padx=10, pady=5)
entry_company_city = ttk.Entry(root)
entry_company_city.grid(row=2, column=1, padx=10, pady=5)
entry_company_city.bind("<Return>", focus_next_widget)

# PDF file name field
ttk.Label(root, text="PDF File Name:").grid(row=3, column=0, padx=10, pady=5)
entry_file_name = ttk.Entry(root)
entry_file_name.grid(row=3, column=1, padx=10, pady=5)
entry_file_name.bind("<Return>", focus_next_widget)

# Client phone number field
ttk.Label(root, text="Client Number:").grid(row=4, column=0, padx=10, pady=5)
entry_client_number = ttk.Entry(root)
entry_client_number.grid(row=4, column=1, padx=10, pady=5)
entry_client_number.bind("<Return>", focus_next_widget)

# Product fields
ttk.Label(root, text="Product Name:").grid(row=5, column=0, padx=10, pady=5)
entry_product_name = ttk.Entry(root)
entry_product_name.grid(row=5, column=1, padx=10, pady=5)
entry_product_name.bind("<Return>", focus_next_widget)

ttk.Label(root, text="Product Price:").grid(row=6, column=0, padx=10, pady=5)
entry_product_price = ttk.Entry(root)
entry_product_price.grid(row=6, column=1, padx=10, pady=5)
entry_product_price.bind("<Return>", focus_next_widget)

ttk.Label(root, text="Quantity:").grid(row=7, column=0, padx=10, pady=5)
entry_product_quantity = ttk.Entry(root)
entry_product_quantity.grid(row=7, column=1, padx=10, pady=5)
entry_product_quantity.bind("<Return>", focus_next_widget)

# Button to add products
button_add_product = ttk.Button(root, text="Add Product", command=add_product)
button_add_product.grid(row=8, column=0, columnspan=2, pady=10)

# Listbox to display products
listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=9, column=0, columnspan=2, pady=10)

# Button to generate invoice
button_generate_invoice = ttk.Button(root, text="Generate Invoice", command=submit_form)
button_generate_invoice.grid(row=10, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
