class StringHandler:
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("")

    def print_string(self):
        print(self.text.upper())
handler = StringHandler()
handler.get_string()
handler.print_string()