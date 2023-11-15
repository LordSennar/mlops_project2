# MLOps Project 2

This project is a Machine Learning Operations example utilizing Docker for containerization and Weights and Biases for experiment tracking.

## Prerequisites

Before you begin, ensure you have the following installed:

- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Docker: [Install Docker](https://docs.docker.com/get-docker/) or Docker Desktop: [Install DockerDesktop](https://www.docker.com/products/docker-desktop/)
- Weights and Biases: [Sign up/in Wandb](https://wandb.ai/site)
- Should have at least 5gb of ram.

## Getting Started

Follow these instructions to set up and run the project.

### 1. Clone the Repository

```bash
git clone https://github.com/LordSennar/mlops_project2.git
cd mlops_project2
```

### 2. Build the Docker Image

```bash
docker build -t mlops_project2 .
```

### 3. Run the Docker Container
Replace <your-wandb-api-key> with the key you got from your wandb project. (40 Characters long)
Or replace the key directly in the Dockerfile, then it isnt needed in this command.
```bash
docker run -e WANDB_API_KEY=<your-wandb-api-key> -e VARIABLE=Value mlops_project2
```
replace VARIABLE with a variable from the list below.

#### Variables for Run

These variables can be used to start a run. 

- LEARNING_RATE=0.0001
- ADAM_EPSILON=0.00000001
- PROJECT_NAME=default_project
- TRAIN_BATCH_SIZE=32
- VAL_BATCH_SIZE=32
- EPOCHS=3
- WARMUP_STEPS=0
- WEIGHT_DECAY=0.0
- LOG_STEP_INTERVAL=50
- SEED=42
- MODEL_SAVE_PATH=models\
- WANDB_API_KEY=<your_wandb_api_key>

## Dockerfile

The Dockerfile uses the python 3.10-slim template. It installs the dependencies and sets the environmental variables.

## main.py

The `main.py` file is the entry point to run the training run. It uses the `model_train.py` file to start the run.
