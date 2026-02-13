import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read-yaml(path_to_yaml: Path) -> ConfigBox
"""reads yaml file and returns

Args:
 Path_to_yaml (str): path like imput
 
 Raises:
  ValueError: if yaml file is empty
  e: empty file
  
  Returns: 
    ConfigBox: ConfigBox type
"""
try:
    With open(path_to_yaml) as yaml_file:
        Content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
except BoxValueError:
    raise ValueError (("yaml file is empty")
except Exception as e:
    raise e
)
