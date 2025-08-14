# Rubik's Cube Solver

An interactive web-based Rubik's Cube solver that visualizes the cube's state and generates step-by-step solutions. This project demonstrates core web development skills using HTML, CSS, and JavaScript, bringing a complex algorithm to life in the browser.

## Table of Contents

  * [Features](https://www.google.com/search?q=%23features)
  * [How It Works](https://www.google.com/search?q=%23how-it-works)
  * [Technologies Used](https://www.google.com/search?q=%23technologies-used)
  * [Getting Started](https://www.google.com/search?q=%23getting-started)
      * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      * [Installation](https://www.google.com/search?q=%23installation)
      * [Usage](https://www.google.com/search?q=%23usage)
  * [Algorithm Details](https://www.google.com/search?q=%23algorithm-details)
  * [Project Structure](https://www.google.com/search?q=%23project-structure)
  * [Future Enhancements](https://www.google.com/search?q=%23future-enhancements)
  * [License](https://www.google.com/search?q=%23license)
  * [Contact](https://www.google.com/search?q=%23contact)

-----

## Features

  * **Interactive Cube Representation:** A visual 3D-like representation of the Rubik's Cube, allowing users to see its state clearly.
  * **Flexible Input Methods:**
      * **Graphical Input:** Click on individual cube stickers and select colors from a palette to set the cube's state.
      * **String Input:** Enter the cube's state as a 54-character string for quick setup.
  * **Standard Cube Rotations:** Buttons to perform common Rubik's Cube moves (e.g., F, B, R, L, U, D) and their inverse counterparts (f, b, r, l, u, d).
  * **Automated Solver:** Generates a sequence of moves to solve the cube from any valid configuration.
  * **Solution Optimization:** Includes logic to compress redundant moves in the solution sequence for brevity.
  * **Orientation Optimization:** The solver attempts to find the shortest solution by trying to solve the cube from all six possible center orientations.
  * **Utility Functions:** "Scramble" to randomize the cube, "Solved State" to reset it, and "Clear All" to refresh the application.
  * **Help Guides:** Provides assistance on cube orientation and input string format.

-----

## How It Works

The solver operates on a digital representation of a 3x3x3 Rubik's Cube. Each of the 54 individual stickers is assigned a color. The core of the application involves:

1.  **State Representation:** The cube's colors are stored and managed in JavaScript arrays, with each array representing a face (Red, White, Orange, Yellow, Blue, Green).
2.  **Move Execution:** JavaScript functions (`F()`, `R()`, etc.) manipulate these arrays to simulate actual cube rotations, updating the visual display accordingly.
3.  **Solving Algorithm:** Upon user request, the solver employs a **Layer-by-Layer (LBL) method**, specifically implementing the **Beginner's Method**. This approach systematically breaks down the complex task of solving the Rubik's Cube into a series of manageable sub-steps.
4.  **Solution Presentation:** The generated sequence of moves is compressed (e.g., `R R R` becomes `r`) and displayed to the user.

-----

## Technologies Used

  * **HTML5:** For structuring the web page content and defining the interactive elements.
  * **CSS3:** For styling the visual appearance, layout (using CSS Grid), and responsiveness of the Rubik's Cube and its controls.
  * **JavaScript (ES5/ES6+):** For managing the cube's state, handling all user interactions, implementing the solving algorithm, and dynamically updating the UI.

-----

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You only need a modern web browser (e.g., Chrome, Firefox, Safari, Edge) to run this application.

### Installation

1.  **Clone the repository (or download the files):**

    ```bash
    git clone <repository-url>
    ```

    (Replace `<repository-url>` with the actual URL of your repository if hosted, otherwise skip this step if you just have the files locally.)

2.  **Navigate to the project directory:**

    ```bash
    cd rubiks-cube-solver
    ```

### Usage

1.  **Open `index.html`:** Simply open the `index.html` file in your preferred web browser.
2.  **Interact with the Solver:**
      * Use the color picking buttons on the left to set the colors of the cube stickers. Click a color, then click a sticker on the cube.
      * Alternatively, input a 54-character string representing the cube's state in the provided text area and click "Enter".
      * Click "Submit" to get the solution.
      * Use "Scramble" to generate a random cube state.
      * Use "Solved State" to reset the cube to its solved configuration.
      * Use the image on the right with defined clickable areas to manually perform moves.

-----

## Algorithm Details

The solver primarily implements the **Beginner's Method**, a step-by-step **Layer-by-Layer (LBL)** approach. This breaks down the solving process into distinct, manageable stages:

1.  **White Cross:** Forming a cross of white edge pieces on one face, correctly aligned with adjacent centers.
2.  **First Layer (F2L-Beginner):** Inserting the four white corner pieces to complete the first layer.
3.  **Second Layer Edges (F2L-Beginner):** Placing the four middle layer edge pieces.
4.  **Yellow Cross:** Creating a cross pattern on the top (yellow) face.
5.  **Orient Last Layer (OLL-Beginner):** Orienting the top layer pieces so all yellow stickers face upwards.
6.  **Permute Last Layer (PLL-Beginner):** Arranging the top layer pieces into their final solved positions.

While the solver's structure follows this Beginner's Method, the project aims to serve as a foundational step towards exploring more advanced methodologies. Specifically, the future goal is to fully incorporate the **CFOP (Cross, F2L, OLL, PLL)** method, which offers more efficient and intuitive algorithms for speedcubing. The current implementation's sub-steps for F2L, OLL, and PLL are broken down more granularly than in a typical CFOP solver, making it an excellent learning tool for the fundamentals before transitioning to advanced techniques.

-----

## Project Structure

```
rubiks-cube-solver/
├── index.html          # Main HTML file for the application layout
├── css/
│   └── Rubik.css       # Stylesheets for the application's visual design
└── js/
    └── Rubik.js        # Core JavaScript logic for cube state, moves, and solving algorithm
└── images/
    ├── Orientation.png # Image explaining cube orientation
    └── Moves.png       # Image showing clickable areas for manual moves
└── README.md           # Project README file
```

-----

## Future Enhancements

  * **Full CFOP Implementation:** Transition from Beginner's Method sub-steps to full CFOP F2L, OLL (57 cases), and PLL (21 cases) algorithms for significantly faster and fewer moves.
  * **Improved UI/UX:** Enhance visual feedback during cube manipulation, potentially adding 3D rendering of the cube.
  * **Algorithm Visualization:** Animate the solution steps or highlight the pieces being moved.
  * **Better Error Messages:** Provide more specific feedback for invalid cube inputs.
  * **Code Refactoring:** Modularize JavaScript code, use modern ES6+ features consistently, and improve readability of the solving logic.
  * **Accessibility:** Ensure the application is accessible to users with disabilities.

