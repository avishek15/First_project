from langchain.llms import CTransformers
from langchain import PromptTemplate
from langchain.chains import LLMChain
from config import model_path

chat_prompt = PromptTemplate.from_template(
    """[INST] <<SYS>>
You are a helpful, respectful and honest assistant. \
Please ensure that your responses are socially \
unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, \
explain why instead of answering something not correct. \
If you don't know the answer to a question, please don't share false information.
The conversation so far has been as follows:
{history}
<</SYS>>

{prompt} [/INST]
    """
)

summary_prompt = PromptTemplate.from_template(
    """[INST] <<SYS>>
You will be given an interaction between you and a human. \
Progressively generate a brief summary, based on the previous \
conversation summary, and the new conversation. The new summary \
should not be more than 100 words.

The conversation summary so far is as follows:
{history}
<</SYS>>

{prompt} [/INST]
{answer_from_ai}
    """
)

llm = CTransformers(model=model_path, model_type="llama")

chat_chain = LLMChain(llm=llm, prompt=chat_prompt, verbose=True)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt, verbose=True)


def conversation(question: str, history: str) -> tuple[str, str]:
    answer = chat_chain(inputs={"history": history, "prompt": question}, return_only_outputs=True)
    # new_history = summary_chain(inputs={"history": history,
    #                                     "prompt": question,
    #                                     "answer_from_ai": answer['text']},
    #                             return_only_outputs=True)
    return answer['text'], ""           # new_history['text']
