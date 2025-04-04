# 🧠 Rover Terrain Classifier (Flask App)

This is a simple Flask application that uses a Decision Tree Classifier model to classify
the terrain into the following categories:
- `Safe`
- `Slippery`
- `Obstacle`
- `Trap`

based on generated data that simulates a rover's sensor measurements.

---

## Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- HTML

---
## Project Structure

/TerrainClassification <br>
├── app.py # Flask application <br> 
├── terrain_classification.pkl # Trained decision tree model <br>
├── terrain_classification.py # File to create decision tree model and save to pkl file <br>
├── model.py # Helper functions to create, train, load, and save model <br>
├── dataset_get.py # Helper functions to generate simulated terrain data <br>
├── /templates <br>
│ └── index.html # Main UI for user input <br>
└── <br>
README.md <br>

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rover-terrain-classifier.git
cd rover-terrain-classifier/TerrainClassification
```

### 2. Install Dependencies

```bash
pip install flask scikit-learn
```

### 3. Create or Add your model

Put your model in the TerrainClassification Directory with the name `terrain_classification.pkl` 
or generate a model using the `terrain_classification.py` file. Feel free to change the ranges of different characteristics and terrain categories in the
`dataset_gen.py` file and the count of generated data types for the model.

### 4. Run the app

```bash
flask run
```

## How to user
1. Enter the five sensor inputs:

* Motor Current (A)
* Vibration Level
* Slip Ratio
* Incline (degrees)
* Obstacle Distance (cm)

2. Click Classify Terrain

3. View the predicted terrain type

## Terrain Type Input Ranges

| Feature               | Unit        | Usable Range(Not validated) | Description                                                  |
|-----------------------|-------------|-----------------------------|--------------------------------------------------------------|
| **Motor Current**     | Amps        | 0.5 – 4.5                   | How hard the motor is working. Higher = resistance/stuck.    |
| **Vibration Level**   | (0–1.5)     | 0.0 – 1.5                   | Bumpiness or shake. Higher = rocky terrain.                  |
| **Slip Ratio**        | (0–1.0)     | 0.0 – 1.0                   | 0 = perfect traction, 1 = lots of slippage.                  |
| **Incline**           | Degrees     | 0 – 30                      | Tilt angle from IMU/accelerometer.                           |
| **Obstacle Height**   | Centimeters | 0 – 30                      | Height of detected obstacle in front of the rover.           |

## Recommended Input Ranges by Terrain Type for pretrained model

| Terrain     | Motor Current (A) | Vibration Level | Slip Ratio | Incline (°) | Obstacle Distance (cm) |
|-------------|-------------------|------------------|-------------|---------------|------------------------|
| **Safe**     | 1.0 – 1.6         | 0.0 – 0.3         | 0.0 – 0.2    | 0 – 10         | 0 – 2                  |
| **Slippery** | 0.8 – 1.3         | 0.2 – 0.6         | 0.5 – 1.0    | 0 – 8          | 0 – 1                  |
| **Obstacle** | 2.0 – 3.5         | 0.5 – 1.2         | 0.2 – 0.6    | 5 – 25         | 5 – 20                 |
| **Trap**     | 2.5 – 4.0         | 0.0 – 0.2         | 0.7 – 1.0    | 0 – 5          | 0 – 3                  |

## License
[MIT License](./LICENSE)

## Author
Built by Damon Rocha — inspired by robotics, nature, and AI to solve real-world problems.