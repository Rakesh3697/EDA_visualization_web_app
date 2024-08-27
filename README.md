# EDA_visualization_web_app
This project is a semi-automated Machine Learning (ML) application built with Streamlit, designed to streamline Exploratory Data Analysis (EDA) and data visualization tasks. The application provides a user-friendly interface to upload datasets, explore their structure, and generate various plots.

## Features

- **Exploratory Data Analysis (EDA)**
  - Upload datasets in CSV, TXT, or XLSX format.
  - Display the dataset's shape, columns, and statistical summary.
  - Filter the dataset by selecting specific columns.
  - Generate value counts and visualize correlation matrices using Matplotlib and Seaborn.
  - Plot pie charts for categorical data.

- **Data Visualization**
  - Upload datasets in CSV, TXT, or XLSX format.
  - Display value counts as bar plots.
  - Generate customizable plots such as area, bar, line, histogram, box, and KDE for selected columns.

## Installation

To run this application locally, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd eda_visualization_web_app

Install the required dependencies:
bash:
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash:
Copy code
streamlit run main.py

Access the app:
The app will open in your default web browser. If not, navigate to http://localhost:8501 in your browser.

Usage:
Exploratory Data Analysis (EDA)

Select "EDA" from the sidebar.
Upload your dataset (CSV or TXT file).
Use the available checkboxes to explore the data (e.g., shape, columns, summary, value counts).
Generate correlation plots or pie charts based on your data.
Data Visualization

Select "Plots" from the sidebar.
Upload your dataset (CSV, TXT, or XLSX file).
Generate value count bar plots or customize your plot by selecting columns and plot types.

This app requires the following Python packages:
streamlit
pandas
numpy
matplotlib
seaborn

These packages are listed in the requirements.txt file and will be installed when you run pip install -r requirements.txt.

Screenshot:
![EDA_screenshot](https://github.com/user-attachments/assets/36cd48f0-54c3-4c29-a8be-28da9cd177e6)


Contributing:
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

License:
This project is licensed under the MIT License. See the LICENSE file for details.
