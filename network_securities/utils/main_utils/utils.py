import yaml
from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging
import os, sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecuritiesException(e, sys)
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            yaml.dump(content, yaml_file)        
    except Exception as e:
        raise NetworkSecuritiesException(e, sys)    
    
def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Saves a numpy array to a file.
    file_path: str location of the file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecuritiesException(e, sys)   

def save_object(file_path: str, obj: object) -> None:
    """
    Saves a Python object to a file using dill.
    file_path: str location of the file to save
    obj: object to save
    """
    try:
        logging.info(f"Saving object to the file path")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved successfully at {file_path}")    
    except Exception as e:
        raise NetworkSecuritiesException(e, sys)     