
from typing import Optional
import pandas as pd
from dataset_hub._core.data_bundle import DataBundle
from dataset_hub._core.get_data import get_data as _get_data


def get_imdb(verbose: Optional[bool] = True) -> pd.DataFrame:
  
    dataset=pd.read_excel("https://raw.githubusercontent.com/laxmimerit/IMDB-Movie-Reviews-Large-Dataset-50k/master/train.xlsx") 
    return dataset