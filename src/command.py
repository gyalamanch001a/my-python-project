class Command:
    def __init__(self):
        import argparse
        self.parser = argparse.ArgumentParser(description="Command-line interface for the router management application.")
        self.setup_commands()

    def setup_commands(self):
        self.parser.add_argument('--login', action='store_true', help='Log in to the router')
        self.parser.add_argument('--process-data', action='store_true', help='Process collected data')
        self.parser.add_argument('--export', type=str, help='Export data to specified format')

    def execute(self):
        args = self.parser.parse_args()
        if args.login:
            self.login()
        elif args.process_data:
            self.process_data()
        elif args.export:
            self.export_data(args.export)
        else:
            self.parser.print_help()

    def login(self):
        print("Logging in to the router...")

    def process_data(self):
        print("Processing data...")

    def export_data(self, format):
        print(f"Exporting data to {format} format...")