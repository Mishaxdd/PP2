class StringHandler:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        """Accepts a string from console input."""
        self.input_string = input()
    def printString(self):
        """Prints the stored string in upper case."""
        print(self.input_string.upper())
if __name__ == "__main__":
    handler = StringHandler()
    handler.getString()
    handler.printString()