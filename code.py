import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    'Machine_ID': np.random.choice([1, 2, 3, 4, 5], size=n),
    'Temperature': np.random.uniform(60, 100, size=n),
    'Run_Time': np.random.uniform(50, 200, size=n),
    'Downtime_Flag': np.random.choice([0, 1], size=n, p=[0.85, 0.15])  # 15% downtime
}

df = pd.DataFrame(data)

df.to_csv('synthetic_manufacturing_data.csv', index=False)
