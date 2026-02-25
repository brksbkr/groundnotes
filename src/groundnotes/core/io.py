from pathlib import Path 
import pandas as pd

def read_table (path: str):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist") 
    if path.suffix.lower() != ".csv":
        raise ValueError("Only .csv files are supported")
    
    # read/return
    df = pd.read_csv(path)
    return df