import pandas as pd
import os
from pathlib import Path

class FileUtil:
    def read_type_mapping_file(self, version="v1"):
        input_df = pd.read_csv(self.get_relative_path("../data/v1/type_mapping.csv"))
        return input_df
    
    def read_entity_file(self, version="v1"):
        input_df = pd.read_csv(self.get_relative_path("../data/v1/entity_list.csv"))
        return input_df
    
    def get_relative_path(self, path_to_file: str):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, path_to_file)
        return Path(__file__).parent / filename
         
