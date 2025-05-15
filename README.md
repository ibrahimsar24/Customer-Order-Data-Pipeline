# 🛠️ Customer Order Data Pipeline Simulation

Simulates a real-world data engineering pipeline using Python, Pandas, and Docker. This project extracts customer order data from JSON files, transforms it into a flat structure, and loads it into both Parquet and CSV formats.

---

## 🚀 Features

- Extracts nested JSON data from one or many files
- Flattens and transforms customer order data
- Calculates total price per item
- Loads final data to:
  - `.parquet` (columnar format)
  - `.csv` (tabular format)
- Designed with modular ETL scripts
- Dockerized for easy execution

---

## 📁 Project Structure

```
customer-order-data-pipeline/
├── data/                   # Input JSON files
├── output/                 # Final outputs (Parquet/CSV)
├── scripts/                # ETL scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── orchestrator.py
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker config
└── README.md               # Project documentation
```

---

## 🔧 Run Locally (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python scripts/orchestrator.py
```

---

## 🐳 Run with Docker (Recommended)

### 1. Build the Docker image:
```bash
docker build -t customer-data-pipeline .
```
> Before this you should login
> ```docker login -u username```

### 2. Run the container:

**On Windows CMD**
```cmd
docker run --rm -v "%cd%":/app customer-data-pipeline
```

**On Linux/macOS**
```bash
docker run --rm -v "$PWD":/app customer-data-pipeline
```

> 💡 This mounts your local folder into the container so that the output `.csv` and `.parquet` files will appear in `output/`.

---

## 📦 Output Sample

Files generated:
- `output/processed_orders.parquet`
- `output/processed_orders.csv`

---

## 🧠 Technologies Used

- Python
- Pandas
- JSON
- PyArrow (for Parquet)
- Docker

---

## 👨‍💻 Author

**Ibrahim Sarguroh**  
📧 [ibrahimsarguroh23@gmail.com](mailto:ibrahimsarguroh23@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ibrahim-sarguroh)  
🔗 [GitHub](https://github.com/ibrahimsar24)

---

## 📌 License

This project is open-source and free to use under the MIT License.
