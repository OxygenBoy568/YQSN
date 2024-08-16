from datetime import datetime

from lagent.actions import ActionExecutor, BingBrowser
from lagent.llms import INTERNLM2_META, LMDeployServer, LMDeployClient

from agent.mindsearch_agent import (MindSearchAgent,
                                               MindSearchProtocol)
from agent.mindsearch_prompt import (
    FINAL_RESPONSE_CN, FINAL_RESPONSE_EN, GRAPH_PROMPT_CN, GRAPH_PROMPT_EN,
    searcher_context_template_cn, searcher_context_template_en,
    searcher_input_template_cn, searcher_input_template_en,
    searcher_system_prompt_cn, searcher_system_prompt_en)

if __name__ == "__main__":
    # bing = BingBrowser(searcher_type='DuckDuckGoSearch', topk=6, proxy = "http://10.99.93.35:8080")
    # print(bing.search("北京"))

    print("创建 LMDeployServer...")
    lang = 'cn'
    llm = LMDeployServer("D:\Kevin\\LLM-Export\\internlm2_5-7b-chat",
                        model_name='internlm2',
                        meta_template=INTERNLM2_META,
                        top_p=0.8,
                        top_k=1,
                        temperature=0,
                        max_new_tokens=8192,
                        repetition_penalty=1.02,
                        stop_words=['<|im_end|>'])
    print("创建 LMDeployServer 完成")
