import pandas as pd
df=pd.read_csv('dataset-1.csv')
df

# Question 1
def generate_car_matrix(df):
  car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
  car_matrix = car_matrix.fillna(0)
  car_matrix.values[[range(len(car_matrix))]*2] = 0
  return car_matrix

car_matrix = generate_car_matrix(df.copy())

# Print the car matrix
print(car_matrix)

# Question 2

def get_type_count(df):
    conditions = [(df['car'] <= 15),(df['car'] > 15) & (df['car'] <= 25),(df['car'] > 25)]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices, right=False)
    type_count = df['car_type'].value_counts().to_dict()
    
    type_count = dict(sorted(type_count.items()))
    return type_count

type_count = get_type_count(df.copy())

# Print the car matrix
print(type_count)

# Question 3

def get_bus_indexes(df):
    mean_bus = df["bus"].mean()
    filtered_df = df[df["bus"] > 2 * mean_bus]
    bus_indexes = sorted(filtered_df.index.to_list())
    return bus_indexes
bus_indexes=get_bus_indexes(df.copy())
bus_indexes

# Question 4

def filter_route(df):
    average_truck_by_route = df.groupby("route")["truck"].mean()
    filtered_routes = average_truck_by_route[average_truck_by_route > 7]
    filtered_route_list = sorted(filtered_routes.index.to_list())
    return filtered_route_list
filtered_route_list=filter_route(df.copy())
filtered_route_list

# Question 5
def multiply_matrix(df):
    
    def multiplier(value):
        
        if value > 20:
            return value * 0.75
        else:
            return value * 1.25
        
        df = df.applymap(multiplier)
        df = df.round(1)
        return df
    df = pd.DataFrame([[10, 25, 15], [20, 30, 10]], columns=['col1', 'col2', 'col3'])
modified_df = multiply_matrix(df.copy())

# Print the modified DataFrame
print(modified_df)

# Question 6 

import pandas as pd
data_2=pd.read_csv('dataset-2.csv')
data_2


def check_timestamp_completeness(data_2):
     def extract_day(startDay):
            return int(startDay.split(" ")[0].split("-")[2])
        
        def extract_time(startTime):
            return pd.to_datetime(timestamp.split(" ")[1]).time()
        
        data_2["time_delta"] = pd.to_timedelta(data_2["endTime"] - data_2["startTime"])
        data_2["start_day"] = data_2["startDay"].apply(extract_day)
        data_2["end_day"] = data_2["endDay"].apply(extract_day)

incomplete_timestamps = (
      (data_2["time_delta"] < pd.Timedelta(hours=24))
      | (data_2["start_time"] != pd.to_datetime("12:00:00"))
      | (data_2["end_time"] != pd.to_datetime("23:59:59"))
      | ((data_2["end_day"] - data_2["start_day"]) != 6)
  )
incomplete_timestamps = incomplete_timestamps.set_index(["id", "id_2"])
return incomplete_timestamps
data_2 = pd.DataFrame({
    "id": [1, 2, 3],
    "id_2": [1, 2, 3],
    "startDay": ["2023-10-26", "2023-10-26", "2023-10-26"],
    "startTime": ["12:00:00", "10:00:00", "11:59:59"],
    "endDay": ["2023-10-27", "2023-10-26", "2023-11-02"],
    "endTime": ["11:59:59", "12:00:00", "23:59:59"],
})

# Check timestamp completeness
incomplete_timestamps = check_timestamp_completeness(df.copy())

# Print the result
print(incomplete_timestamps)

