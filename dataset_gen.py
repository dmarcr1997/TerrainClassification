import random
from enum import Enum

# Create enum class for different TerrainTypes
class TerrainType(Enum):
    Safe = 1
    Slippery = 2
    Obstacle = 3
    Trap = 4

def generate_terrain_data(data_type: TerrainType, data_count: int):
    """Generates random terrain data based on Terrain type"""
    # Caching variables
    sample_data = [] 
    motor_current = 0.0
    vibration = 0.0
    slippage = 0.0
    incline = 0.0
    obstacle = 0.0
    # Range to generate specific amount of data
    for _ in range(data_count):
        current_noise = random.uniform(-0.1, 0.1)
        vibration_noise = random.uniform(-0.05, 0.05)
        slip_noise = random.uniform(-0.05, 0.05)
        incline_noise = random.uniform(-1, 1)
        obstacle_noise = random.uniform(-1, 1)

        match(data_type):
            case TerrainType.Safe:
                # Generates safe numbers in random ranges
                motor_current = random.uniform(1.0, 1.6)
                vibration = random.uniform(0.0, 0.3)
                slippage = random.uniform(0.0, 0.2)
                incline = random.uniform(0.0, 10.0)
                obstacle = random.uniform(0.0, 2.0)

            case TerrainType.Slippery:
                # Generates slippery numbers in random ranges
                motor_current = random.uniform(0.8, 1.3)
                vibration = random.uniform(0.2, 0.6)
                slippage = random.uniform(0.5, 1.0)
                incline = random.uniform(0.0, 8.0)
                obstacle = random.uniform(0.0, 1.0)

            case TerrainType.Obstacle:
                # Generates obstacle numbers in random ranges
                motor_current = random.uniform(2.0, 3.5)
                vibration = random.uniform(0.5, 1.2)
                slippage = random.uniform(0.2, 0.6)
                incline = random.uniform(5.0, 25.0)
                obstacle = random.uniform(5, 20.0)

            case TerrainType.Trap:
                # Generates trap numbers in random ranges
                motor_current = random.uniform(2.5, 4.0)
                vibration = random.uniform(0.0, 0.2)
                slippage = random.uniform(0.7, 1.0)
                incline = random.uniform(0.0, 5.0)
                obstacle = random.uniform(0.0, 3.0)

            case _:
                # Invalid TerrainType used as parameters
                return
        
        # Add noise for model overfitting 
        motor_current += current_noise
        vibration += vibration_noise
        slippage += slip_noise
        incline += incline_noise
        obstacle += obstacle_noise   
    
        # Add data to sample_data array
        sample_data.append({"label": data_type.name, "data": [motor_current, vibration, slippage, incline, obstacle]}) 
    return sample_data

def generate_terrain_dataset():
    """Generates the 100 items for each TerrainType"""
    dataset = [
        generate_terrain_data(TerrainType.Safe, 100), 
        generate_terrain_data(TerrainType.Slippery, 100), 
        generate_terrain_data(TerrainType.Obstacle, 100),
        generate_terrain_data(TerrainType.Trap, 100)    
    ]
    # Flatten the list of lists into a single list
    flattened_dataset = [item for sublist in dataset for item in sublist]
    # Shuffle the dataset in place
    random.shuffle(flattened_dataset)
    return flattened_dataset
    
# run generate_terrain_dataset
# used to test out logic of this file
if __name__ == "__main__":
    print(f"DATA:\n{generate_terrain_dataset()}")
