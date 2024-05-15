
import os
import torch
import transformers


os.environ["HF_HOME"] = "~/.huggingface"
os.environ["HF_TOKEN"] = "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"


def load_pipeline():
    model_id = "meta-llama/Meta-Llama-3-8B"

    pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
    )
    return pipeline

def get_result(prompt):
    pipeline = load_pipeline()
    return pipeline(prompt)


# ~/.cache/huggingface/
