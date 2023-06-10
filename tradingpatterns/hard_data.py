import pandas as pd
def generate_sample_df_with_pattern(pattern):
    date_rng = pd.date_range(start='1/1/2020', end='1/10/2020', freq='D')
    data = {'date': date_rng}
    if pattern == 'Head and Shoulder':
        data['Open'] = [90, 85, 80, 90, 85, 80, 75, 80, 85, 90]
        data['High'] = [95, 90, 85, 95, 90, 85, 80, 85, 90, 95]
        data['Low'] = [80, 75, 70, 80, 75, 70, 65, 70, 75, 80]
        data['Close'] = [90, 85, 80, 90, 85, 80, 75, 80, 85, 90]
        data['Volume'] = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    elif pattern == 'Inverse Head and Shoulder':
        data['Open'] = [20, 25, 30, 20, 25, 30, 35, 30, 25, 20]
        data['High'] = [25, 30, 35, 25, 30, 35, 40, 35, 30, 25]
        data['Low'] = [15, 20, 25, 15, 20, 25, 30, 25, 20, 15]
        data['Close'] = [20, 25, 30, 20, 25, 30, 35, 30, 25, 20]
        data['Volume'] = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    elif pattern == "Double Top" or "Double Bottom" or "Ascending Triangle" or "Descending Triangle":
        data['High'] = [95, 90, 85, 95, 90, 85, 80, 85, 90, 95]
        data['Low'] = [80, 75, 70, 80, 75, 70, 65, 70, 75, 80]
        df = pd.DataFrame(data)
        df.iloc[3:5,1] =100
        df.iloc[6:8,1] =70
        df.iloc[6:9,2] =70
    df = pd.DataFrame(data)
    return df