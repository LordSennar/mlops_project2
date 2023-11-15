# MLOps Project 2

This project is an Machine Learning Operations example utilizing Docker for containerization and Weights and Biases for experiment tracking.

## Prerequisites

Before you begin, ensure you have the following installed:

- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Docker: [Install Docker](https://docs.docker.com/get-docker/)

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

```bash
docker run -e WANDB_API_KEY=your-wandb-api-key -e Variable=Value mlops_project2
```

#### Variables for Run

These variables can be used to start a run. The WANDB_API_KEY can be directly replaced in the Dockerfile, then it isnt needed in the run-command.

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

