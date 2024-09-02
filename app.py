import sqlite3
import os
from enum import Enum

con = sqlite3.connect("cars.db")
cur = con.cursor()

# Create a table if there isn't one already
cur.execute("CREATE TABLE IF NOT EXISTS Cars(Customer TEXT, Color TEXT, Brand TEXT)")

class MENU(Enum):
    Add_Customer = 1
    Add_Car = 2
    Show_All = 3
    Edit = 4
    Search = 5
    Delete = 6
    Save = 7
    Load = 8
    Exit = 9

def menu():
    for item in MENU: 
        print(f'{item.value} - {item.name.replace("_", " ")}')
    return MENU(int(input("Your Selection: ")))

# Adds a new customer to the list
def AddCustomer(Customer, carColor, carBrand):
    cur.execute("INSERT INTO Cars VALUES(?, ?, ?)", (Customer, carColor, carBrand))
    print(f"New customer name is {Customer} and their new car is: {carColor} {carBrand}")

# Checks if a customer exists in the list
def customer_exists(customer_name):
    cur.execute("SELECT * FROM Cars WHERE Customer = ?", (customer_name,))
    return cur.fetchone() is not None

# Adds new cars if there is a matching customer name on the list
def AddCarInfo(Customer, carColor, carBrand):
    if customer_exists(Customer):
        cur.execute("INSERT INTO Cars VALUES(?, ?, ?)", (Customer, carColor, carBrand))
        print(f"Car added for {Customer}: {carColor} {carBrand}")
    else:
        print(f"{Customer} not found")

# Edits a car's info on the list
def EditList(Customer, oldColor, oldBrand, newColor, newBrand):
    if customer_exists(Customer):
        cur.execute("UPDATE Cars SET Color=?, Brand=? WHERE Customer=? AND Color=? AND Brand=?",
                    (newColor, newBrand, Customer, oldColor, oldBrand))
        print(f"Car of {Customer} updated to: {newColor} {newBrand}")
    else:
        print(f"{Customer} not found")

# Searches for cars in the list by customer name and car color/brand
def search(Customer, carColor, carBrand):
    cur.execute("SELECT * FROM Cars WHERE Customer=? AND Color=? AND Brand=?", 
                (Customer, carColor, carBrand))
    found = cur.fetchall()
    if found:
        for car in found:
            print(f"Found: {car}")
    else:
        print(f"No car found for {Customer} with Color: {carColor} and Brand: {carBrand}")

# Deletes cars from the list
def deleteCar(Customer, carColor, carBrand):
    cur.execute("DELETE FROM Cars WHERE Customer=? AND Color=? AND Brand=?", 
                (Customer, carColor, carBrand))
    print(f"The {carColor} {carBrand} of {Customer} has been deleted")

# Shows all info on the list
def Show_All():
    res = cur.execute("SELECT * FROM Cars")
    for i in res.fetchall():
        print(i)

# Saves the current data to the database
def Save():
    con.commit()
    print("Changes have been saved.")

# Loads data from the database
def Load():
    global con, cur
    con.close()  # Close the existing connection
    con = sqlite3.connect("cars.db")
    cur = con.cursor()
    print("Data has been loaded.")

# Exits the selection screen, asks to save, and closes the database connection
def Exit_screen():
    save = input("Do you want to save the changes before exiting? (yes/no): ").strip().lower()
    if save == "yes":
        Save()
    else:
        con.rollback()
        print("Changes have not been saved.")
    con.close()
    exit()

if __name__ == "__main__":
    while True:
        UserSelection = menu()
        if UserSelection == MENU.Add_Customer:
            AddCustomer(
                input("New Customer Name: "),
                input("Car Color: "),
                input("Car Brand: ")
            )
        elif UserSelection == MENU.Add_Car:
            AddCarInfo(
                input("Customer Name: "),
                input("Car Color: "),
                input("Car Brand: ")
            )
        elif UserSelection == MENU.Show_All:
            Show_All()
        elif UserSelection == MENU.Edit:
            EditList(
                input("Customer Name: "),
                input("Old Car Color: "),
                input("Old Car Brand: "),
                input("New Car Color: "),
                input("New Car Brand: ")
            )
        elif UserSelection == MENU.Search:
            search(
                input("Customer Name: "),
                input("Car Color: "),
                input("Car Brand: ")
            )
        elif UserSelection == MENU.Delete:
            deleteCar(
                input("Customer Name: "),
                input("Car Color: "),
                input("Car Brand: ")
            )
        elif UserSelection == MENU.Save:
            Save()
        elif UserSelection == MENU.Load:
            Load()
        elif UserSelection == MENU.Exit:
            Exit_screen()
