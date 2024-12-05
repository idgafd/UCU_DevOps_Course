# Iris Flower Prediction Web App

A Flask-based machine learning web application for predicting the type of Iris flower. Users can manually input features through a web interface or use a REST API for programmatic predictions. Includes visual feedback with flower images.

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/idgafd/UCU_DevOps_Course.git
cd UCU_DevOps_Course/ml-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Access the app at: [http://localhost:8050](http://localhost:8050)

## Docker Deployment

### Build the Docker Image

```bash
docker build -t idgafd/ml-app:multistage .
```

### Run the Container

```bash
docker run -it --rm -p 8050:8050 idgafd/ml-app:multistage
```

Open your browser at: [http://localhost:8050](http://localhost:8050)
