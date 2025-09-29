class EmailLayout:
    def __init__(self, recipient_name, sender_name):
        self.recipient_name = recipient_name
        self.sender_name = sender_name

    def __enter__(self):
        print(f"Hello {self.recipient_name}\n")

    def __exit__(self, exc_type, exc_value, traceback):
        print("\nBest Regards,")
        print(self.sender_name)

