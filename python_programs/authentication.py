# authentication.py

class Authentication:
    def __init__(self):
        # For simplicity, let's define hardcoded credentials
        self.valid_credentials = {"1234": "5678"}  # Card number: PIN

    def authenticate(self, card_number, pin):
        if card_number in self.valid_credentials and self.valid_credentials[card_number] == pin:
            return True
        else:
            return False
