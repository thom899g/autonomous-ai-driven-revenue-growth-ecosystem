import logging
from typing import Dict, Any
import yaml

class ConfigurationManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)