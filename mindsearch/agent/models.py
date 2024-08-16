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
                       model_name='internlm2',
                      # model_name = "mannix/internlm2.5-20b:latest",
                     # model_name = "qwen2:latest",
                    #  url='http://127.0.0.1:23333',
                     #   model_name='internlm/internlm2.5:latest',
                       url = "http://localhost:11434",
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
            model_type='gpt-4-turbo',
            key=os.environ.get('OPENAI_API_KEY', 'YOUR OPENAI API KEY'))
