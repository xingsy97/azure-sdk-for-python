from promptflow import tool
from azureml.metrics import compute_metrics, constants
from azureml.metrics.common.exceptions import ValidationException
from promptflow.connections import AzureOpenAIConnection
from utils import get_openai_parameters


@tool
def evaluate_groundedness(
                      chat: list[str],
                      connection: AzureOpenAIConnection,
                      deployment_name: str
                      ) -> dict:
    y_pred = [chat]
    openai_params = get_openai_parameters(connection, deployment_name)

    metrics_config = {
        "openai_params": openai_params,
        # set this to True/False based on description above
        "use_chat_completion_api": True,
        # If we want the model to use previous conversation context
        # set this value to True
        # Note: Setting this value to True increases reliability of
        # metrics but might be expensive
        "use_previous_conversation": False
    }
    metrics = ["gpt_groundedness"]
    try:
        result = compute_metrics(task_type=constants.Tasks.RAG_EVALUATION,
                                 y_pred=y_pred,
                                 metrics=metrics,
                                 **metrics_config)
    except ValidationException:
        result = None
    return result
