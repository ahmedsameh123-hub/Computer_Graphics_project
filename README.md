# Computer Graphics Project

This project is a unified interactive graphics application using **Pygame** and **OpenGL** for CSE382.  
It demonstrates analytical and practical solutions for 10 fundamental computer graphics questions, each with user controls to modify parameters in real time.

---

## Project Structure

```
cg_project
├── src
│   ├── main.py        # Entry point of the application
│   └── utils.py       # Utility functions for drawing and transformations
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```


## Requirements

- Python 3.x
- Pygame
- PyOpenGL
- numpy

Install dependencies with:

## Running the Application

To start the application, navigate to the `src` directory and run the `main.py` file:

```
cd src
python main.py
```

## Usage

Once the application is running, you can interact with the graphics using keyboard inputs. The application supports various functionalities that can be explored through the user interface.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

---


## Application Usage

- **Switch between questions:**  
  Press keys `1` to `9` for questions 1-9, and `0` for question 10.

- **Modify parameters:**  
  Each question has its own interactive controls.  
  Use the following keys (depending on the question):

| Question | What it does                        | Controls (while on this question)                |
|----------|-------------------------------------|--------------------------------------------------|
| 1        | Translation, rotation, scaling      | Arrows: move, W/S: scale, A/D: rotate            |
| 2        | Camera movement                     | Arrows/W/S: move camera                         |
| 3        | Clock stretching                    | W/S: stretch                                    |
| 4        | Reflection over line                | Arrows: move point, W/S: slope, A/D: intercept   |
| 5        | Composite transform                 | W/S: change parameter a                         |
| 6        | Shear/taper/scale/rotate/translate  | W/S: shear, A/D: rotate                         |
| 7        | Square rotate/translate             | Arrows: move, A/D: rotate                       |
| 8        | Cube scaling                        | W/S: scale X, A/D: scale Y, Q/E: scale Z        |
| 9        | Cube rotation                       | A/D: rotate                                     |
| 10       | Scale, rotate, translate cube       | W/S: scale X, A/D: scale Y, Q/E: scale Z,<br>Arrows: move, Z/X: rotate |

- **Exit:**  
  Press `ESC` or close the window.

---

## Notes

- Each question visualizes a different transformation or concept.
- All code is in `main.py` for easy review and grading.
- Analytical solutions (mathematical explanation and numpy/matplotlib code) are provided separately in the report as required by the project specification.

---

## Contribution

Feel free to suggest improvements or report issues.

---

**Good luck!**