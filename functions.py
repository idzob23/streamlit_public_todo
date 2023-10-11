FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local   # you can also put global variable todos instead of return, but return is better

def write_todos(todos_arg, filepath=FILEPATH):  #first argument cannot be default
    """ Write to-do items in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

###################################################################################################
# This code bellow will be executed only if you explicitly run this file
# If the file is imported or called from another file __name__ will not be equual to __main__
# good for testing :-)
# __name__  is only equal   __main__    when run thos file directly.
# when imported then __name__ is equal to functions
###################################################################################################

if __name__ == "__main__":
    print("Hello")
    print(get_todos())