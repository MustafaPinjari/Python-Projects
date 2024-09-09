# 🌳 Fractal Tree Pattern using Turtle 🐢

Welcome to the Fractal Tree Pattern project! This project creates beautiful fractal trees using Python's Turtle graphics. 🌲🌳

## 📋 Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Credits](#credits)
- [License](#license)

## 🌟 Introduction

This project demonstrates how to create fractal tree patterns using recursive functions in Python. The Turtle module is used to draw these stunning tree patterns. Each tree is drawn with different colors and recursion depths, creating a visually appealing design. 🎨

## 🛠 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Fractal-Tree-Pattern.git
    cd fractal-tree-pattern
    ```

2. **Install the necessary libraries:**

    Ensure you have Python installed on your system. This project uses the Turtle graphics module, which is included with Python's standard library.

## 🚀 Usage

To run the fractal tree pattern script, use the following command:

```bash
python fractal_tree.py
```

This will open a window displaying the fractal tree patterns. Each pattern is drawn with different colors and recursion depths.

## 🖥 Code Explanation

The script uses a recursive function to draw each segment of the tree. The `draw` function is called with different lengths and colors to create the fractal pattern. Here's a brief explanation of the key parts of the code:

- **Setting up the Turtle and Screen:**

    ```python
    import turtle as tu

    roo = tu.Turtle()
    wn = tu.Screen()
    wn.bgcolor("black")
    wn.title("Fractal Tree Pattern")
    roo.left(90)
    roo.speed(0)
    ```

- **Recursive Drawing Function:**

    ```python
    def draw(l, color, factor):
        if l < 10:
            return
        roo.pensize(2)
        roo.pencolor(color)
        roo.forward(l)
        roo.left(30)
        draw(factor * l, color, factor)
        roo.right(60)
        draw(factor * l, color, factor)
        roo.left(30)
        roo.backward(l)
    ```

- **Drawing the Patterns:**

    Multiple calls to the `draw` function are made with different parameters to create the various tree patterns:

    ```python
    draw(20, "magenta", 3/4)
    draw(40, "lightgreen", 4/5)
    draw(60, "cyan", 6/7)
    ```

## 🙏 Credits

This project was created by Mustafa Pinjari. You can find more of my work on my [GitHub](https://github.com/MustafaPinjari), [LinkedIn](https://www.linkedin.com/in/mustafa-pinjari-287625256/), and [Instagram](https://www.instagram.com/its_ur_musuuu).

Special thanks to the creators of the Python Turtle module for providing such a fun and versatile tool for creating graphics. 🐢

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
