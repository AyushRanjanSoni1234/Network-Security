import sys
import os 
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from network_securities.constant.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from network_securities.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from network_securities.entity.config_entity import DataTransformationConfig
from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging

from network_securities.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)
        
    def get_data_transformer_object(cls) -> Pipeline:  
        """
        It creates a data transformation pipeline with KNN imputer for handling missing values.
        Returns:
            Pipeline: A scikit-learn Pipeline object that contains the KNN imputer.
        """  
        logging.info(f"Creating data transformation pipeline with KNN imputer for handling missing values")
        try:
            knn_imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            pipeline = Pipeline(steps=[
                ("KNNImputer", knn_imputer)
            ])
            return pipeline
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info(f"Initiating data transformation starts now")
        try:
            logging.info(f"Reading training and testing file")

            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            ## Training DataFrame
            logging.info(f"Splitting input and target feature from training and testing dataframe")
            x_train = train_df.drop(TARGET_COLUMN, axis=1)
            y_train = train_df[TARGET_COLUMN]
            y_train = y_train.replace(-1, 0)

            # Testing DataFrame
            x_test = test_df.drop(TARGET_COLUMN, axis=1)
            y_test = test_df[TARGET_COLUMN]
            y_test = y_test.replace(-1, 0)

            logging.info(f"Imputing missing values in training and testing dataframe using KNN imputer")
            preprocessor = self.get_data_transformer_object()

            transformed_input_train_data = preprocessor.fit_transform(x_train)
            transformed_input_test_data = preprocessor.transform(x_test)

            logging.info(f"Saving transformed training and testing input data to numpy array")

            train_array = np.c_[transformed_input_train_data, np.array(y_train)]
            test_array = np.c_[transformed_input_test_data, np.array(y_test)]

            ## Save the train and test arrays and preprocessor object
            logging.info(f"Saving preprocessor object")    
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_array)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_array)

            ## Prepare artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path
            )

            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecuritiesException(e, sys)