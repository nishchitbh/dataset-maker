# Dataset Maker

Dataset Maker is a simple tool designed to assist machine learning developers in creating demo datasets for their projects. It provides a graphical interface where you can click on a grid to mark points and assign them different colors. The clicked points are saved in a JSON file, which can be used as a dataset for training or testing machine learning models.

## Features

- Click on the grid to mark points with different colors.
- Remove points by clicking on them again.
- Points are saved in a JSON file for easy retrieval.
- Customize the grid size and units per division.
- Choose from a variety of color options.
- Clear all points with a single click.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone or download this repository.
2. Install the required dependencies by running the following command:

```
pip install pygame
```
## Usage

1. Run the `main.py` script to start the program:
2. The main window will appear, showing a grid and color options.
3. Click on the grid to mark points with the selected color.
4. Click on a marked point to remove it.
5. The clicked points are automatically saved in the `dataset.json` file.
6. Use the generated `dataset.json` file as a dataset for your machine learning project.
    
```
python main.py
```

## Customization

- Adjust the grid size and units per division:
- Open the `main.py` file in a text editor.
- Modify the `units_per_division` variable to change the number of units per grid division.
- The overall grid size will automatically adjust accordingly.

- Customize the color options:
- Open the `main.py` file in a text editor.
- Modify the `color_options` dictionary to add, remove, or modify color options.
- Colors should be specified as RGB tuples.

## Contributing

Contributions to improve the Dataset Maker tool are welcome! If you encounter any issues, have suggestions, or would like to add new features, please feel free to submit a pull request.
