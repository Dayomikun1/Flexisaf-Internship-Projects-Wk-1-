# Python Mini Projects 🎮📊

This repository contains a collection of beginner-friendly Python mini-projects:
- 🎮 Rock, Paper, Scissors – A classic console game
- ❌⭕ Tic-Tac-Toe – Play against a simple AI
- 📊 Sales Data Visualization – Simple charts using real sales data

---

## 📁 Project Structure

```
├── Rock, Paper, Scissors.py       # Classic Rock-Paper-Scissors game
├── Tic-Tac-Toe.py                 # Tic-Tac-Toe with AI (no external libs)
├── company_sales_data.csv         # Dataset used for visualization
├── Data Visualization.ipynb       # Script to generate sales and profit charts
├── README.md                      # Project documentation
├── LICENSE                        # MIT License
```

---

## 🎮 Rock, Paper, Scissors

### Description
A terminal-based game where you play against a pseudo-random computer opponent by choosing rock, paper, or scissors.

### Run the Game
```bash
python "Rock, Paper, Scissors.py"
```

### Features
- Input validation
- Randomized computer choice (no `random` module)
- Determines winner or draw

---

## ❌⭕ Tic-Tac-Toe

### Description
Play as "X" in a 3x3 grid against an AI player ("O"). The AI picks moves randomly from available spots using a pseudo-random approach.

### Run the Game
```bash
python "Tic-Tac-Toe.py"
```

### Features
- Validates moves
- Detects wins and ties
- Simple pseudo-AI without `random` module

---

## 📊 Sales Data Visualization

### Description
Uses `company_sales_data.csv` to generate charts showing:
- Monthly total sales
- Monthly total profits

### Dependencies
Install required packages:
```bash
pip install matplotlib pandas
```

### Run the Visualization
```
To run the visualization within Jupyter Notebook:

Open the notebook file (visualize_sales.ipynb) in Jupyter Notebook.

Run the cells in the notebook to generate the sales visualizations.
```

### Expected Charts
- 📈 Line chart of monthly profit
- 📊 Bar chart of monthly total sales

---

## ✅ Requirements

- Python 3.x
- `matplotlib` (for charting)
- `pandas` (for data handling)

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](./LICENSE) file for more information.

---

## 🙌 Contributions

Feel free to fork the project, make enhancements, and submit pull requests!
Suggestions include:
- Adding GUI using tkinter or pygame
- Improving AI for Tic-Tac-Toe
- Extending visualizations (e.g. by product/profit)

---

## ✨ Author

Created with ❤️ for learning and fun.
