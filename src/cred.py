class Credentials:
    def __init__(self):
        self.username = None
        self.password = None

    def load_credentials(self):
        # Load credentials from environment variables or a secure vault
        import os
        self.username = os.getenv('ROUTER_USERNAME')
        self.password = os.getenv('ROUTER_PASSWORD')

    def get_credentials(self):
        if self.username is None or self.password is None:
            self.load_credentials()
        return self.username, self.password