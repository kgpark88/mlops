import mlflow

experiment_name = "Ridge"
entry_point = "Training2"

mlflow.set_tracking_uri("http://127.0.0.1:5000")

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
)
