# Implementation Steps

Follow these steps to set up and run the project.

## Step 1: Clone the Repository
Clone the repository using your preferred method (HTTPS, SSH, or GitHub CLI).

```bash
git clone [text](https://github.com/Advait-Pade/Binary-Classification-of-Insurance-Cross-Selling.git)
```

## Step 2: Create a Virtual Environment
Create a virtual environment using the following command:

```bash
python -m venv env
```

## Step 3: Activate the Virtual Environment
Activate the virtual environment using the command below, depending on your operating system:

- **Windows:**
  ```bash
  env\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source env/bin/activate
  ```

## Step 4: Install Dependencies
Install the required dependencies using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Step 5: Run the MLflow Server
Run the MLflow server to access model experiments and deployed models.

```bash
mlflow server --host 0.0.0.0 --port 8080
```

Access the MLflow server at:
- [http://localhost:8080](http://localhost:8080)
- [http://your_ip_address:8080](http://your_ip_address:8080)

## Step 6: Run the Insurance Prediction Application
Run the Insurance Prediction application using the following command:

```bash
python app.py
```

Access the application at:
- [http://localhost:5000](http://localhost:5000)
