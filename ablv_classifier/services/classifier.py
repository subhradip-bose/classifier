from presidio_analyzer import AnalyzerEngine
from ablv_classifier.utils.file_util import  FileUtil  
from ablv_classifier.transformer.sentance_transfomer import Transformer

class TextClassifier:
    """
    This class holds all the wrapper logic for Text classifications ...

    Attributes:
        analyzer : Presidio analyzer object
        mapping_file (Pandas dataframe): Mapping file loaded as Pandas dataframe
        entity_file (Pandas dataframe): Entity(used in presidio analyzer) file loaded as Pandas dataframe
        mappings (List[string]) : List of entities
        default_language (string) : Default language for classification
        similar_items   : A list of similar items for a give entity
    Methods:
        classfyText(self, arg1) -> list[dict]: A list of extracted classfication values
        
    """
    def __init__(self) -> None:
        self.analyzer = AnalyzerEngine()
        self.mapping_file  = FileUtil().read_type_mapping_file()
        self.entity_file =  FileUtil().read_entity_file()
        self.entities =  self.entity_file['Entity Type'].tolist()
        self.mappings =  self.mapping_file['PII_Type'].tolist()
        self.default_language = "en"
        self.similar_items = self.load_tarnsformers()

    def classfyText(self, text:str) :
        results = self.analyzer.analyze(text=text,
                           entities=self.entities,
                           language=self.default_language)
        if  results:
            return self.map_output(results)
        return  {} 
    
    def extract_value(self, dict: {}):
        for value in dict.values():
            return value

    
    def process(self, df, score):
        list_of_elements = []
        dict = df.to_dict()
        list_of_elements.append(self.extract_value(dict["PII_Type"]))
        list_of_elements.append(self.extract_value(dict["HIPAA_Protected_Health_Information_Category"]))
        list_of_elements.append(self.extract_value(dict["DHS_Category"])) 
        list_of_elements.append(self.extract_value(dict["Risk_Level"]))  
        list_of_elements.append(self.calculate_risk_level(score))    
        return list_of_elements
             
    def calculate_risk_level(self, scrore):
        if scrore >= 0.6 :
            return "High probability"
        elif scrore < 0.6 and scrore >= 0.3 :
            return "Medium probability"
        else:
            return "Low probability"
            


    def map_output(self, result:[]):
        list_of_dict = {}
        for individual in result:
            dict = individual.to_dict()
            entity_type = dict["entity_type"]
            filter_df = self.mapping_file.loc[self.mapping_file['PII_Type'] == entity_type]
            if not filter_df.empty:
               list_of_dict[entity_type] = self.process(filter_df,  dict["score"])
            else:
                entity_type = self.similar_items[entity_type][0]
                filter_df = self.mapping_file.loc[self.mapping_file['PII_Type'] == entity_type]
                list_of_dict[entity_type] = self.process(filter_df,  dict["score"])
        return list_of_dict

    def load_tarnsformers(self):
        tranformer =   Transformer()
        model =  tranformer.load_model()
        return tranformer.cosine_similarity(model, self.entities, self.mappings)


