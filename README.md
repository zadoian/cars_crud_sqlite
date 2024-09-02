
# Car Management Application

This is a simple command-line application for managing customer car information using Python and SQLite. The application allows you to add customers, add cars, view all records, edit records, search for specific cars, delete records, save changes to the database, and load data from the database.

## Features

- **Add Customer:** Add a new customer along with their car's color and brand.
- **Add Car:** Add a new car for an existing customer.
- **Show All:** Display all records in the database.
- **Edit:** Modify the details of an existing car record.
- **Search:** Search for a specific car by customer name, color, and brand.
- **Delete:** Remove a car record from the database.
- **Save:** Save changes made during the session to the database.
- **Load:** Reload data from the database, discarding unsaved changes.
- **Exit:** Exit the application with an option to save changes.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite3 (included with Python)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/car-management-app.git
   cd car-management-app
   ```

2. **Run the application:**

   ```bash
   python yourscriptname.py
   ```

### Usage

Upon running the script, you'll be presented with a menu of options. Enter the number corresponding to the action you'd like to take.

### Example

1. **Adding a Customer:**
   - Select `1 - Add Customer`
   - Enter the customer's name, car color, and car brand.

2. **Adding a Car:**
   - Select `2 - Add Car`
   - Enter the existing customer's name, car color, and car brand.

3. **Saving Changes:**
   - Select `7 - Save` to commit your changes to the database.

4. **Loading Data:**
   - Select `8 - Load` to reload data from the database.

5. **Exiting the Application:**
   - Select `9 - Exit`. You will be prompted to save changes before exiting.

### Database

The application uses an SQLite database (`cars.db`) to store customer and car information. This database is created automatically if it does not exist.

### Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
