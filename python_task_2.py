import pandas as pd
df=pd.read_csv('dataset-3.csv')
df

# Question 1
def calculate_distance_matrix(df):
    
    distance_dict = {}
    

    for _, row in df.iterrows():
        
        start_toll = row["id_start"]
        end_toll = row["id_end"]
        distance = row["distance"]
        distance_dict[(id_start, id_end)] = distance
        distance_dict[(id_end, id_start)] = distance
        
        toll_locations = set(df["id_start"]).union(df["id_end"])
        distance_matrix = pd.DataFrame(index=toll_locations, columns=toll_locations)
        
        for start_toll in toll_locations:
            visited = set()
            unvisited = {toll: float("inf") for toll in toll_locations}
            unvisited[id_start] = 0
    
    while unvisited:
         current_toll = min(unvisited, key=unvisited.get)
            visited.add(current_toll)
        
    

    for neighbor_toll in toll_locations:
    
        if neighbor_toll not in visited:
            
            new_distance = unvisited[current_toll] + distance_dict.get((current_toll, neighbor_toll), float("inf"))
            distance_matrix.loc[id_start] = unvisited
                        
distance_matrix.values[::len(distance_matrix) + 1] = 0
return distance_matrix
distance_matrix = calculate_distance_matrix(df.copy())

# Print the distance matrix
print(distance_matrix)


# Question 2

def unroll_distance_matrix(distance_matrix):
    
    toll_locations = list(distance_matrix.index)
    unrolled_matrix = pd.DataFrame(columns=["id_start", "id_end", "distance"])
    
for i in range(len(toll_locations)):
    
    for j in range(len(toll_locations)):
        
        if i != j:
            unrolled_matrix = unrolled_matrix.append({
            "id_start": toll_locations[i],
            "id_end": toll_locations[j],
            "distance": distance_matrix.iloc[i, j],
        }, 
                ignore_index=True)
        return unrolled_matrix
unrolled_matrix = unroll_distance_matrix(distance_matrix.copy())
unrolled_matrix

# Question 3

def find_ids_within_ten_percentage_threshold(df, reference_id):
    filtered_df = df[df["id_start"] == reference_id]
    average_distance = filtered_df["distance"].mean()
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1
    filtered_df = filtered_df[(filtered_df["distance"] >= lower_bound) & (filtered_df["distance"] <= upper_bound)]
    filtered_ids = sorted(filtered_df["id_start"].to_list())
    return filtered_ids
filtered_ids = find_ids_within_ten_percentage_threshold(df.copy(),1)
filtered_ids

# Question 4 

def calculate_toll_rate(df, rate_coefficients):
     for vehicle_type, rate_coefficient in rate_coefficients.items():
            
            df[vehicle_type] = df["distance"] * rate_coefficient
            return df
        df = calculate_toll_rate(df.copy(), rate_coefficients)
        df

# Question 5 

# Didn't Get Output
