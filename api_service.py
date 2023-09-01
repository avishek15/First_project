from Llama2_chat import conversation
from fastapi import FastAPI

conversation_history = ""
app = FastAPI()


@app.get("/")
def main(query: str) -> str:
    global conversation_history
    answer, conversation_history = conversation(query, conversation_history)
    print(f"```{conversation_history=}```")
    return answer

# if __name__ == '__main__':
#     while True:
#         question = input("Ask me anything: ")
#         if question == 'q':
#             break
#         print(main(question))
