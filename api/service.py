import ollama
from typing import List, Dict


gemma2 = "gemma2"
llm_options = {
    "temperature": 0,
    "num_ctx": 2048,
    "num_predict": 4096,
    "top_k": 20,
    "top_p": 0.95,
}


def _gen_content(
    prompts:List,
    system_prompt:str=None,
    model:str="llama3.2",
    options:Dict=None) -> str:

    if options is None:
        options = {}

    messages = []
    if system_prompt is not None:
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    for prompt in prompts:
        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

    res = ollama.chat(
        model=model,
        messages=messages,
        options=options,
        stream=False
    )

    return res['message']['content']


def chat(message:str):
    msg = _gen_content(
        prompts=[message],
        model=gemma2,
        options=llm_options)
    return {"message": msg, "context": "assistant"}
