from lagent.actions import ActionExecutor, BingBrowser
from lagent.llms import INTERNLM2_META, LMDeployServer, LMDeployClient, HFTransformerCasualLM,GPTAPI
from openai import OpenAI

if __name__ == "__main__" :

    # client = OpenAI(
    #     api_key="eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE1MzgxMCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzc4MTI1MCwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU2ODQwNTQwNTAiLCJ1dWlkIjoiZDY4OTYxOTEtYzA2Ny00YzFjLTk5NTktOTY0ZmM2NmYyMWM0IiwiZW1haWwiOiIiLCJleHAiOjE3MzkzMzMyNTB9.ZAwYBGJMJXiEvoTlyvtzK0kgWu-ZPYAZ7xwsmYv6SUZjoTVPnRrSSQIW-SfiRaZwR-Nt4HB6prCnlFRRUqr_kg",  # 此处传token，不带Bearer
    #     base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
    # )

    # chat_rsp = client.chat.completions.create(
    #     model="internlm2.5-latest",
    #     messages=[{"role": "user", "content": "你是谁？"}],
    # )

    # for choice in chat_rsp.choices:
    #     print(choice.message.content)
    
    # internlm_client = dict(type=LMDeployClient,
    #                    model_name='internlm2',
    #                    url = "http://localhost:11434",
    #                 #    model_name='internlm2.5-latest',
    #                 #    url = "https://internlm-chat.intern-ai.org.cn/puyu/api/",
    #                 #    api_key = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE1MzgxMCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzc4MTI1MCwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU2ODQwNTQwNTAiLCJ1dWlkIjoiZDY4OTYxOTEtYzA2Ny00YzFjLTk5NTktOTY0ZmM2NmYyMWM0IiwiZW1haWwiOiIiLCJleHAiOjE3MzkzMzMyNTB9.ZAwYBGJMJXiEvoTlyvtzK0kgWu-ZPYAZ7xwsmYv6SUZjoTVPnRrSSQIW-SfiRaZwR-Nt4HB6prCnlFRRUqr_kg",
    #                    meta_template=INTERNLM2_META,
    #                    top_p=0.8,
    #                    top_k=1,
    #                    temperature=0,
    #                    max_new_tokens=8192,
    #                   # max_new_tokens=2000,
    #                    repetition_penalty=1.02,
    #                    stop_words=['<|im_end|>'])
    
    #   llm = LMDeployClient(url = "http://localhost:11434", 
    #                     # model_name='internlm/internlm2.5:latest',
    #                      model_name = "internlm2:latest",
    #                      meta_template=INTERNLM2_META,
    #                      top_p=0.8,
    #                      top_k=1,
    #                      temperature=0,
    #                      max_new_tokens=8192,
    #                      repetition_penalty=1.02,
    #                      stop_words=['<|im_end|>'])
    llm = GPTAPI(
       model_type='internlm2.5-latest',
        key='eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE1MzgxMCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzc4MTI1MCwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU2ODQwNTQwNTAiLCJ1dWlkIjoiZDY4OTYxOTEtYzA2Ny00YzFjLTk5NTktOTY0ZmM2NmYyMWM0IiwiZW1haWwiOiIiLCJleHAiOjE3MzkzMzMyNTB9.ZAwYBGJMJXiEvoTlyvtzK0kgWu-ZPYAZ7xwsmYv6SUZjoTVPnRrSSQIW-SfiRaZwR-Nt4HB6prCnlFRRUqr_kg')
      
    print(llm.chat("你是谁？"))