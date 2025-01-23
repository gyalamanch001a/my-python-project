import asyncio
import sys
import time
from loggs import Logger
from cred import Credentials
from vedge_login import VedgeLogin
from ios_login import IosLogin
from data_processing import DataProcessor
from command import Command

def main():
    startTime = time.strftime('%Y-%m-%d_%H.%M.%S')
    logger = Logger(startTime)
    
    credentials = Credentials()
    routers = []
    routes = []
    
    command = Command()
    command.parse_arguments()
    
    if command.no_debug:
        logger.disable_debug()
    
    logger.log_info("Starting the application...")
    
    vedge_login = VedgeLogin(credentials)
    ios_login = IosLogin(credentials)
    
    # Example of logging into routers
    routers.extend(vedge_login.login())
    routers.extend(ios_login.login())
    
    # Process data
    data_processor = DataProcessor()
    processed_data = data_processor.process(routes)
    
    # Save results
    data_processor.export_results(processed_data, startTime)
    
    logger.log_info("Application finished successfully.")

if __name__ == "__main__":
    asyncio.run(main())