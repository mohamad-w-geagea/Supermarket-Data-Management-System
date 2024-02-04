class ProductNode:
    def __init__(self, product_data):
        self.product_data = product_data
        self.next = None


class BrandNode:
    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.products = None
        self.next = None


class CategoryNode:
    def __init__(self, category_name):
        self.category_name = category_name
        self.brands = None
        self.left = None
        self.right = None


class CategoryBST:
    def __init__(self):
        self.root = None

    def insert_category(self, category_name):
        category_name = category_name.lower()
        self.root = self._insert_category_helper(self.root, category_name)

    def _insert_category_helper(self, node, category_name):
        if node is None:
            return CategoryNode(category_name)

        if category_name < node.category_name:
            node.left = self._insert_category_helper(node.left, category_name)
        else:
            node.right = self._insert_category_helper(node.right, category_name)

        return node

    def find_category(self, category_name):
        category_name = category_name.lower()
        return self._find_category_helper(self.root, category_name)

    def _find_category_helper(self, node, category_name): 
        if node is None or category_name == node.category_name:
            return node

        if category_name < node.category_name:
            return self._find_category_helper(node.left, category_name)
        else:
            return self._find_category_helper(node.right, category_name)
   
    def print_all_categories(self):
        self._print_all_categories_helper(self.root)

    def _print_all_categories_helper(self, node):
        if node is not None:
            self._print_all_categories_helper(node.left)
            print("Category:", node.category_name)
            self._print_all_categories_helper(node.right)
    

class BrandLinkedList:
    def __init__(self):
        self.head = None

    def insert_brand(self, brand_name):
        new_node = BrandNode(brand_name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def find_brand(self, brand_name):
        current = self.head
        while current is not None:
            if current.brand_name == brand_name:
                return current
            current = current.next
        return None
    

class ProductInventory:
    def __init__(self):
        self.categories = CategoryBST()

    def insert_product(self, name, category, brand, price, quantity):
        category_node = self.categories.find_category(category)
        if category_node is None:
            self.categories.insert_category(category)
            category_node = self.categories.find_category(category)

        brand_list = category_node.brands
        if brand_list is None:
            brand_list = BrandLinkedList()
            category_node.brands = brand_list

        brand_node = brand_list.find_brand(brand)
        if brand_node is None:
            brand_list.insert_brand(brand)
            brand_node = brand_list.find_brand(brand)

        product_data = {
            "name": name,
            "category": category,
            "brand": brand,
            "price": price,
            "quantity": quantity
        }
        new_product = ProductNode(product_data)

        if brand_node.products is None:
            brand_node.products = new_product
        else:
            current = brand_node.products
            while current.next is not None:
                current = current.next
            current.next = new_product

    def search_product(self, category, brand, name):
        category_node = self.categories.find_category(category)
        if category_node is None:
            print("Category not found.")
            return

        brand_list = category_node.brands
        if brand_list is None:
            print("Brand not found.")
            return

        brand_node = brand_list.find_brand(brand)
        if brand_node is None:
            print("Brand not found.")
            return
        current = brand_node.products
        while current is not None:
            if current.product_data["name"] == name:
                print("Product found:", current.product_data)
                return
            current = current.next

        print("Product not found.")
    def get_product_price(self, category, brand, name):
        category_node = self.categories.find_category(category)
        if category_node is None:
            print("Category not found.")
            return None

        brand_list = category_node.brands
        if brand_list is None:
            print("Brand not found.")
            return None

        brand_node = brand_list.find_brand(brand)
        if brand_node is None:
            print("Brand not found.")
            return None

        current = brand_node.products
        while current is not None:
            if current.product_data["name"] == name:
                return current.product_data["price"]
            current = current.next

        print("Product not found.")
        return None

    def sell_product(self, category, brand, name, quantity):
        category_node = self.categories.find_category(category)
        if category_node is None:
            print("Category not found.")
            return

        brand_list = category_node.brands
        if brand_list is None:
            print("Brand not found.")
            return

        brand_node = brand_list.find_brand(brand)
        if brand_node is None:
            print("Brand not found.")
            return

        current = brand_node.products
        while current is not None:
            if current.product_data["name"] == name:
                if current.product_data["quantity"] >= quantity:
                    current.product_data["quantity"] -= quantity
                    print("Product sold:", current.product_data)
                else:
                    print("Quantity in stock is limited to", current.product_data["quantity"])
                return
            current = current.next

        print("Product not found.")
    def print_all_brands(self, category_name):
        category_node = self.categories.find_category(category_name.lower())
        if category_node is None:
            print("Category not found.")
            return

        brand_list = category_node.brands
        if brand_list is None or brand_list.head is None:
            print("No brands found for the category.")
            return

        current = brand_list.head
        while current is not None:
            print("Brand:", current.brand_name)
            current = current.next

class SalesLogQueue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue_sale(self, name, category, brand, price):
        sale_data = {
            "name": name,
            "category": category,
            "brand": brand,
            "price": price
            }
        new_sale = ProductNode(sale_data)

        if self.head is None:
            self.head = new_sale
            self.tail = new_sale
        else:
            self.tail.next = new_sale
            self.tail = new_sale

    def dequeue_sale(self):
        if self.head is None:
            return None

        removed_sale = self.head.product_data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_sale
    def print_sales_log(self):
        current = self.head

        if current is None:
            print("Sales log is empty.")
            return

        while current is not None:
            print("Product:", current.product_data)
            current = current.next
