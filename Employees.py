class EmployeeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class EmployeeBST:
    def __init__(self):
        self.root = None

    def build_employee_tree(self, employee_list):
        for data in employee_list:
            self.add_employee(data)

    def add_employee(self, data):
        employee_name = data["name"].lower()
        new_node = EmployeeNode(data)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if employee_name < current_node.data["name"].lower():
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    current_node = current_node.right

   
    def search_employee(self, employee_name):
        employee_name = employee_name.lower()
        current_node = self.root

        while current_node is not None:
            if employee_name == current_node.data["name"].lower():
                print("Employee found:", current_node.data)
                return  
            elif employee_name < current_node.data["name"].lower():
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        print("Employee not found.")


    def remove_employee(self, employee_name):
        employee_name = employee_name.lower()
        self.root, removed_employee = self._remove_employee_helper(self.root, employee_name)
        if removed_employee:
            print("Employee removed:", removed_employee)
        else:
            print("Employee not found.")

    def _remove_employee_helper(self, node, employee_name):
        if node is None:
            return None, None

        if employee_name < node.data["name"].lower():
            node.left, removed_employee = self._remove_employee_helper(node.left, employee_name)
        elif employee_name > node.data["name"].lower():
            node.right, removed_employee = self._remove_employee_helper(node.right, employee_name)
        else:
            removed_employee = node.data
            if node.left is None:
                return node.right, removed_employee
            elif node.right is None:
                return node.left, removed_employee
            else:
                successor_parent = node
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                if successor_parent != node:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

                node.data = successor.data

        return node, removed_employee

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    def _find_min_node(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def edit_employee(self, employee_name, property_key, new_value):
        employee_name = employee_name.lower()
        current_node = self.root
        found = False

        while current_node is not None:
            if employee_name == current_node.data["name"].lower():
                found = True
                break
            elif employee_name < current_node.data["name"].lower():
                current_node = current_node.left
            else:
                current_node = current_node.right

        if found == True :
            if property_key in current_node.data:
                current_node.data[property_key] = new_value
                print("Employee data updated.")
            else:
                print("Invalid property key.")
        else:
            print("Employee not found.")
            return

    def print_all_employees(self):
        self._print_all_employees_helper(self.root)

    def _print_all_employees_helper(self, node):
        if node is not None:
            self._print_all_employees_helper(node.left)
            print("Employee:", node.data)
            self._print_all_employees_helper(node.right)    
