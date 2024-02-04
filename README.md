# Supermarket Management System

## Project Overview

This project involves designing and implementing a system to manage data for a big supermarket. The system is tasked with handling information related to supermarket employees and product inventory. The operations include adding, removing, searching, and editing employee data, as well as inserting, selling, and searching for products. Additionally, a sales log needs to be maintained independently of the product inventory.

## Data Structures

### Employees
The employee data is stored in a Binary Search Tree (BST) where each node contains a dictionary object with employee information (name, position, age, and salary). The name of the employee is used as the key in the BST.

### Product Inventory
The product data is organized using a combination of data structures:
- Categories are stored in a BST.
- Each category node points to a Linked List containing brand names related to the category.
- Each brand node points to another Linked List storing the products related to the category and brand.

### Sales Log
Sales logs are stored using a Queue data structure, where each node is similar to a product node but without the quantity attribute.

## Operations

### Employees
- **Build the employee tree using given employee data.**
- **Add Employee:** Take input for name, position, age, and salary.
- **Search for Employee:** Take input for the employee name.
- **Remove Employee:** Take input for the employee name to search and remove if found.
- **Edit Employee Data:** Take input for the employee name, the property to change, and its new value.

### Product Inventory
- **Build the category/brand/product data structure using given product data.**
- **Insert Product:** Take input for name, category, brand, price, and quantity.
- **Search for Product:** Take input for product category, brand, and name.
- **Sell Product:** Take input for product category, brand, name, and quantity to purchase.
- **Show Sales Log:** Display the sales log queue.
- **Print all Categories:** Traverse the category tree and print names.
- **Print all Brands for a Category:** Take a category name as input, traverse the brand list, and print brand names.

## Menu

In the main file, a menu will be presented to the user with options to interact with either Employees or Product Inventory. Based on the chosen category, specific options are displayed:

### Employees
1. **Add Employee**
2. **Search for an Employee**
3. **Remove an Employee**
4. **Edit Employee Data**
5. **Print all Employees**

### Product Inventory
1. **Insert Product**
2. **Search for a Product**
3. **Sell Product**
4. **Show Sales Log**
5. **Print all Categories**
6. **Print all Brands for a category**

Users can choose an action, and the corresponding function will be executed as described in the Operations section.

## Implementation

To run the system, execute the main file. The menu will guide you through the available actions for managing employees and product inventory.

**Note:** Ensure you have the necessary input files for employee and product data provided as part of the project files.
