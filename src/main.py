import argparse
import wandb
from model_train import ModelTrain

def main():
    parser = argparse.ArgumentParser(description="Runs GLUETransformer once")
    parser.add_argument("-lr", dest="learning_rate", type=float, default=1e-4, help="Learning rate used for training. Default is 1e-4")
    parser.add_argument("-adam_epsilon", dest="adam_epsilon", type=float, default=1e-8, help="Adam epsilon for training. Default is 1e-8")
    parser.add_argument("-project_name", dest="project_name", default="project2", help="Project name used in weights and biases. Default is 'project2'")
    parser.add_argument("-train_batch_size", dest="train_batch_size", type=int, default=128, help="Training batch size. Default is 128")
    parser.add_argument("-val_batch_size", dest="val_batch_size", type=int, default=128, help="Validation batch size. Default is 128")
    parser.add_argument("-epochs", dest="epochs", type=int, default=3, help="Number of training epochs. Default is 3")
    parser.add_argument("-warmup_steps", dest="warmup_steps", type=int, default=2, help="Number of warmup steps. Default is 2")
    parser.add_argument("-weight_decay", dest="weight_decay", type=float, default=0.001, help="Weight decay parameter. Default is 1e-3")
    parser.add_argument("-log_step_interval", dest="log_step_interval", type=int, default=50, help="Logging step interval. Default is 50")
    parser.add_argument("-seed", dest="seed", type=int, default=42, help="Random seed for reproducibility. Default is 42")
    parser.add_argument("-model_save_path", dest="model_save_path", default="models/", help="Path to save the trained model. Default is 'models/'")
    parser.add_argument("-wandb_key", dest="wandb_key", required=True, help="Weights and Biases API key")

    args = parser.parse_args()

    learning_rate = args.learning_rate
    adam_epsilon = args.adam_epsilon
    project_name = args.project_name
    train_batch_size = args.train_batch_size
    val_batch_size = args.val_batch_size
    epochs = args.epochs
    warmup_steps = args.warmup_steps
    weight_decay = args.weight_decay
    log_step_interval = args.log_step_interval
    seed = args.seed
    model_save_path = args.model_save_path

    print("Parameters:")
    for arg, value in vars(args).items():
        if arg != "wandb_key":
            print(f"{arg}: {value}")

    wandb.login(key=args.wandb_key)

    mct = ModelTrain(project_name=project_name,
                     model_save_path=model_save_path,
                     train_batch_size=train_batch_size,
                     val_batch_size=val_batch_size,
                     epochs=epochs,
                     warmup_steps=warmup_steps,
                     weight_decay=weight_decay,
                     log_step_interval=log_step_interval,
                     seed=seed)

    mct.train_run(learning_rate=learning_rate, adam_epsilon=adam_epsilon)

if __name__ == "__main__":
    main()
