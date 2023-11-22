import os
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)05d | %(levelname)s | %(filename)s:%(lineno)d | %(message)s' , datefmt='%FY%T')

class ApplicationConfiguration:

    REPO_HOST: str = "127.0.0.1"
    REPO_PORT: int = 1234
    
    DB_NAME: str = "timer_db"
    DB_USER: str = "root" #TODO: Move to secrets
    DB_PASSWORD: str = "1234" #TODO: Move to secrets

    RECONNECT_WAIT_TIME: int = 1

    RETRY_NUMBER: int = 10

    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Start App")

        self.extract_env_variables()
        

    def extract_env_variables(self):
        for attr, attr_type in self.__annotations__.items():
            try:
                self.__setattr__(attr, (attr_type)(os.environ[attr]))
            except Exception as err:
                self.logger.warning(f"Couldn't find {attr} in environment. Run with default")
        
app_config = ApplicationConfiguration()