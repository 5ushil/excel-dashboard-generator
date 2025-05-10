Here's a **professional `README.md`** file that you can use for your project. It includes all the necessary sections to explain how to run the app, what it does, and its dependencies.

---

## 📊 Excel Dashboard Generator

A simple yet powerful tool to convert Excel files into interactive dashboards and professional HTML reports using **Streamlit**, **Plotly**, and **Jinja2**.

---

### 🧰 Features

- ✅ Upload `.xlsx` files
- ✅ Auto-detect numerical and categorical columns
- ✅ Generate line charts for numeric trends
- ✅ Compare categories with bar charts
- ✅ Export styled HTML report with:
  - First few rows of data
  - Summary statistics
  - Interactive Plotly chart embedded

---

### 📁 Project Structure

```
excel_dashboard/
│
├── app.py              # Main Python script
├── templates/
│   └── report.html     # Jinja2 HTML template for reporting
├── requirements.txt    # Python package dependencies
└── reports/            # (Auto-created) Folder to store generated HTML reports
```

---

### 🛠️ Technologies Used

| Tool        | Purpose |
|-------------|---------|
| **Streamlit** | Build interactive web dashboard |
| **Pandas** | Read and manipulate Excel data |
| **Plotly Express** | Create beautiful visualizations |
| **Jinja2** | Generate HTML reports dynamically |
| **Openpyxl** | Support for `.xlsx` file format |

---

### 🚀 How to Run

#### 1. Clone or download this repository

```bash
git clone https://github.com/yourusername/excel-dashboard-generator.git
cd excel-dashboard-generator
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you're using Python 3.8+

#### 3. Run the App

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

### 📄 Usage Instructions

1. Click **"Upload your Excel file (.xlsx)"**
2. Select the sheet you want to analyze
3. The app will automatically:
   - Show raw data
   - Detect numeric & categorical columns
   - Generate trend or comparison charts
4. Download an **HTML report** with all insights included

---

### 📝 Requirements (`requirements.txt`)

```txt
streamlit
pandas
plotly
jinja2
openpyxl
```

---

### 📂 Templates (`templates/report.html`)

The HTML report is built using a Jinja2 template, which includes:

- Title and date
- First 5 rows of data
- Summary statistics
- Embedded Plotly chart

You can customize the styling in `report.html` as needed.

---

### 📁 Reports Output

After generating a report, it will be saved in the `reports/` folder with a timestamped name.

---

### ⚠️ Notes

- This version does **not support PDF export** to avoid Windows compatibility issues.
- All visualizations are interactive thanks to **Plotly**.
- UTF-8 encoding is used throughout to ensure compatibility with special characters.

---

### 📦 Optional: Create Executable (Windows)

To turn this into a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "templates;templates" app.py
```

Your users can now double-click to run the app without installing anything.

---

### 💡 Want More?

Let me know if you'd like help adding features like:

- PDF report export
- AI-generated insights
- Multi-user login
- Deployment on Streamlit Cloud

---

## 🙌 License

MIT License – feel free to modify and distribute!

---

## 📬 Feedback / Contributions

Contributions welcome! If you find any bugs or have suggestions, please open an issue or submit a pull request.
