import os

from lagent.llms import (GPTAPI, INTERNLM2_META, HFTransformerCasualLM,
                         LMDeployClient, LMDeployServer)

# qwen_client = dict(type=LMDeployClient,
#                        model_name='qwen2:latest',
#                        url='http://localhost:11434/v1',
#                        meta_template=INTERNLM2_META,
#                        top_p=0.8,
#                        top_k=1,
#                        temperature=0,
#                        max_new_tokens=8192,
#                        repetition_penalty=1.02,
#                        stop_words=['<|im_end|>'])

internlm_server = dict(type=LMDeployServer,
                       path='D:\Kevin\\LLM-Export\\internlm2_5-7b-chat',
                      # path = "D:\Kevin\LLM-Export\internlm2_5-20b-chat",
                       model_name='internlm2',
                       meta_template=INTERNLM2_META,
                       top_p=0.8,
                       top_k=1,
                       temperature=0,
                       max_new_tokens=8192,
                       repetition_penalty=1.02,
                       stop_words=['<|im_end|>'])

internlm_client = dict(type=LMDeployClient,
                       model_name='internlm2:latest',
                       url = "http://localhost:11434",
                      #  model_name='internlm2.5-latest',
                      #  url = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
                      #  api_key = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE1MzgxMCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzc4MTI1MCwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU2ODQwNTQwNTAiLCJ1dWlkIjoiZDY4OTYxOTEtYzA2Ny00YzFjLTk5NTktOTY0ZmM2NmYyMWM0IiwiZW1haWwiOiIiLCJleHAiOjE3MzkzMzMyNTB9.ZAwYBGJMJXiEvoTlyvtzK0kgWu-ZPYAZ7xwsmYv6SUZjoTVPnRrSSQIW-SfiRaZwR-Nt4HB6prCnlFRRUqr_kg",
                       meta_template=INTERNLM2_META,
                       top_p=0.8,
                       top_k=1,
                       temperature=0,
                       max_new_tokens=8192,
                      # max_new_tokens=2000,
                       repetition_penalty=1.02,
                       stop_words=['<|im_end|>'])


internlm_hf = dict(type=HFTransformerCasualLM,
                  #  path='internlm/internlm2_5-7b-chat',
                  path = "D:\\Kevin\\LLM-Export\\internlm2_5-7b-chat",
                   meta_template=INTERNLM2_META,
                   top_p=0.8,
                   top_k=None,
                   temperature=1e-6,
                   max_new_tokens=8192,
                   repetition_penalty=1.02,
                   stop_words=['<|im_end|>'])

gpt4 = dict(type=GPTAPI,
            model_type='internlm2.5-latest',
            key='eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE1MzgxMCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzc4MTI1MCwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU2ODQwNTQwNTAiLCJ1dWlkIjoiZDY4OTYxOTEtYzA2Ny00YzFjLTk5NTktOTY0ZmM2NmYyMWM0IiwiZW1haWwiOiIiLCJleHAiOjE3MzkzMzMyNTB9.ZAwYBGJMJXiEvoTlyvtzK0kgWu-ZPYAZ7xwsmYv6SUZjoTVPnRrSSQIW-SfiRaZwR-Nt4HB6prCnlFRRUqr_kg',
            openai_api_base = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions"
            )