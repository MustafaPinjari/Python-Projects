# 🧾 Invoice Generator 📄

Welcome to the **Invoice Generator** project! This Python application helps you create and manage professional PDF invoices with ease. It provides a user-friendly interface for inputting company details, product information, and client details, and generates a well-formatted invoice that includes a company logo and an option to send the invoice via WhatsApp.

## 🌟 Features

- **Company and Product Details**: Easily input company information and product details.
- **Logo Integration**: Add a company logo to your invoices.
- **Currency Support**: Uses Indian Rupees (₹) as the currency symbol.
- **WhatsApp Integration**: Send the generated invoice directly to a client's WhatsApp number using Twilio's API.
- **Interactive Interface**: User-friendly GUI with dynamic fields and functionality.

## 📸 Screenshots

![Invoice Generator Screenshot](/Images/APP.png)
*User Interface of the Invoice Generator*

![Sample Invoice](/Downloads/ca.pdf)
*Preview of a Generated Invoice*

## 🛠️ Prerequisites

Before you get started, ensure you have the following:

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **Twilio Account**: Sign up for a Twilio account for WhatsApp messaging.

## 🚀 Installation

Follow these steps to set up and run the Invoice Generator:

1. **Clone the Repository**

   Download the project files using Git:

   ```bash
   git clone https://github.com/MustafaPinjari/invoice-generator.git
   cd invoice-generator
   ```

2. **Install Required Packages**

   Install the necessary Python packages using `pip`:

   ```bash
   pip install reportlab
   pip install pillow
   pip install twilio
   ```

3. **Configure Twilio**

   - Sign up for a [Twilio account](https://www.twilio.com/).
   - Set up a WhatsApp sandbox or a business number.
   - Replace placeholders in the code with your Twilio credentials (account SID, auth token, and WhatsApp number).

## 🏃‍♂️ Usage

1. **Run the Application**

   Start the application by running the Python script:

   ```bash
   python invoice_generator.py
   ```

2. **Enter Details**

   - Input company details (name, address, city).
   - Add product details (name, price, quantity).
   - Generate the invoice and save it as a PDF.
   - Send the invoice to the client's WhatsApp number if desired.

3. **View and Send the Invoice**

   The generated PDF invoice will be saved in your `Downloads` folder. You can also send it directly to the client's WhatsApp through the application.


## 💬 Credits

- **Developer:** Mustafa Pinjari 👨‍💻  
[GitHub](https://github.com/MustafaPinjari)</br>
[LinkedIn](https://www.linkedin.com/in/mustafa-pinjari-287625256/).  

  A special thanks to all contributors and the open-source community for their support and resources! 🙌

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🚀 Get Started Today!

Start using the Invoice Generator to streamline your invoicing process. If you have any questions or need assistance, feel free to reach out!

Happy invoicing! 😊
