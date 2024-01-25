import pandas as pd

class FileUtil:
    def read_type_mapping_file(self, version="v1"):
        input_df = pd.read_csv("ablv_classifier/data/v1/type_mapping.csv")
        return input_df
    
    def read_entity_file(self, version="v1"):
        input_df = pd.read_csv("ablv_classifier/data/v1/entity_list.csv")
        return input_df
         
