import argparse
import pandas as pd
from typing import Text
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

from src.utils.logs import get_logger

def featurize(config_path: Text) -> None:
    """Create new features.
    Args:
        config_path {Text}: path to config
    """

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logger = get_logger('FEATURIZE', log_level=config['base']['log_level'])

    logger.info('Load raw data')
    dataset = pd.read_csv(config['data_load']['dataset_prepare'])

    ####### DROP UNUSED COLUMNS #######
    logger.info('Drop unused columns')
    cols_to_drop = config['featurize']['cols_to_drop']
    df = dataset.drop(cols_to_drop, axis=1)

    ####### DEFINE CORRELATED FEATURES #######
    logger.info('Proccess correlated features')
    corr_vars1 = config['featurize']['corr_vars1']
    corr_vars2 = config['featurize']['corr_vars2']

    # Scaling
    df1 = df[corr_vars1]
    df2 = df[corr_vars2]

    # Standard and transform to normal distribution
    sc = StandardScaler()
    fit_df = sc.fit_transform(df1)
    df_1 = pd.DataFrame(fit_df,columns=df1.columns)

    fit_df2 = sc.fit_transform(df2)
    df_2 = pd.DataFrame(fit_df2,columns=df2.columns)

    # Unifying
    pca = PCA(n_components=1)
    new_var1 = pca.fit_transform(df_1)
    new_var2 = pca.fit_transform(df_2)

    # Update dataset
    df_data_reduced = pd.concat((df, pd.DataFrame(new_var1)), axis=1)
    df_data_reduced.rename({0: 'grp1_corrvars'}, axis=1, inplace = True)
    df_data_reduced.drop(corr_vars1, axis=1, inplace=True)

    df_data_reduced = pd.concat((df_data_reduced, pd.DataFrame(new_var2)), axis=1)
    df_data_reduced.rename({0: 'grp2_corrvars'}, axis=1, inplace = True)
    df_data_reduced.drop(corr_vars2, axis=1, inplace=True)

    df = df_data_reduced

    ####### PREPARE CATEGORICAL FEATURES ####### 
    logger.info('Proccess categorical features')
    categorical_vars = config['featurize']['categorical_vars']

    encoder = OneHotEncoder(sparse_output=False)
    #Create a DataFrame with the one-hot encoded columns
    #We use get_feature_names_out() to get the column names for the encoded data
    one_hot_encoded = encoder.fit_transform(df[categorical_vars])

    #Create a DataFrame with the one-hot encoded columns
    #We use get_feature_names_out() to get the column names for the encoded data
    one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_vars))

    # Concatenate the one-hot encoded dataframe with the original dataframe
    df_encoded = pd.concat([df, one_hot_df], axis=1)

    # Drop the original categorical columns
    df_encoded = df_encoded.drop(categorical_vars, axis=1)

    df = df_encoded

     ####### SAVE FEATURES ####### 
    logger.info('Save features')
    features_path = config['featurize']['features_path']
    df.to_csv(features_path, index=False)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    featurize(config_path=args.config)