# escape=`
# changed the \ to the current escape value to prevent clashes with the windows pathsystem
# Project 2 MLOps HS23 MI
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV LEARNING_RATE=0.0001 `
    ADAM_EPSILON=0.00000001 `
    PROJECT_NAME=project2 `
    TRAIN_BATCH_SIZE=128 `
    VAL_BATCH_SIZE=128 `
    EPOCHS=3 `
    WARMUP_STEPS=2 `
    WEIGHT_DECAY=0.003 `
    LOG_STEP_INTERVAL=50 `
    SEED=42 `
    MODEL_SAVE_PATH=models\ `
    WANDB_API_KEY=<insert_your_wandb_key>

CMD python ./src/main.py -wandb_key $WANDB_API_KEY -lr $LEARNING_RATE -adam_epsilon $ADAM_EPSILON -project_name $PROJECT_NAME -train_batch_size $TRAIN_BATCH_SIZE -val_batch_size $VAL_BATCH_SIZE -epochs $EPOCHS -warmup_steps $WARMUP_STEPS -weight_decay $WEIGHT_DECAY -log_step_interval $LOG_STEP_INTERVAL -seed $SEED -model_save_path $MODEL_SAVE_PATH
