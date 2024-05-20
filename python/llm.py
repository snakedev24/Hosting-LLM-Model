
import os
import torch
import transformers


os.environ["HF_HOME"] = "~/.huggingface"
os.environ["HF_TOKEN"] = "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"


def load_pipeline():
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

    pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
    )
    return pipeline

def get_result(user_prompt):
    pipeline = load_pipeline()

    messages = [
    {"role": "system", "content": "You are a chatbot who always responds with a answer or greeting. You are talking to a user who is asking you a question."},
    {"role": "user", "content": f"{user_prompt}"},
    ]

    prompt = pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
    )

    
    return outputs[0]["generated_text"][len(prompt):]


# ~/.cache/huggingface/
