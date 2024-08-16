from datetime import datetime

from lagent.actions import ActionExecutor, BingBrowser
from lagent.llms import INTERNLM2_META, LMDeployServer, LMDeployClient, HFTransformerCasualLM

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
    # llm = LMDeployServer(# path='internlm/internlm2_5-7b-chat',
    #                     "D:\\Kevin\\LLM-Export\\internlm2_5-7b-chat",
    #                     model_name='internlm2',
    #                     meta_template=INTERNLM2_META,
    #                     top_p=0.8,
    #                     top_k=1,
    #                     temperature=0,
    #                     max_new_tokens=8192,
    #                     repetition_penalty=1.02,
    #                     stop_words=['<|im_end|>'])
    
    llm = LMDeployClient(url = "http://localhost:11434", 
                        # model_name='internlm/internlm2.5:latest',
                        model_name = "internlm2",
                         meta_template=INTERNLM2_META,
                         top_p=0.8,
                         top_k=1,
                         temperature=0,
                         max_new_tokens=8192,
                         repetition_penalty=1.02,
                         stop_words=['<|im_end|>'])

    # llm = HFTransformerCasualLM(
    #     path = "D:\\Kevin\\LLM-Export\\internlm2_5-7b-chat",
    #     meta_template=INTERNLM2_META,
    #     top_p=0.8,
    #     top_k=None,
    #     temperature=1e-6,
    #     max_new_tokens=8192,
    #     repetition_penalty=1.02,
    #     stop_words=['<|im_end|>']
    # )
    
    # print("生成...")
    # prompt = "你是谁？"
    # print (llm.generate(inputs = prompt))

    print("创建 MindSearchAgent...")
    agent = MindSearchAgent(
        llm=llm,
        protocol=MindSearchProtocol(
            meta_prompt=datetime.now().strftime('The current date is %Y-%m-%d.'),
            interpreter_prompt=GRAPH_PROMPT_CN
            if lang == 'cn' else GRAPH_PROMPT_EN,
            response_prompt=FINAL_RESPONSE_CN
            if lang == 'cn' else FINAL_RESPONSE_EN),
        searcher_cfg=dict(
            llm=llm,
            plugin_executor=ActionExecutor(
                BingBrowser(searcher_type='DuckDuckGoSearch', topk=6, proxy = "http://10.99.93.35:8080")),
            protocol=MindSearchProtocol(
                meta_prompt=datetime.now().strftime(
                    'The current date is %Y-%m-%d.'),
                plugin_prompt=searcher_system_prompt_cn
                if lang == 'cn' else searcher_system_prompt_en,
            ),
            template=dict(input=searcher_input_template_cn
                        if lang == 'cn' else searcher_input_template_en,
                        context=searcher_context_template_cn
                        if lang == 'cn' else searcher_context_template_en)),
        max_turn=10)

    print("发起提问...")
    for agent_return in agent.stream_chat('上海今天适合穿什么衣服'):
        # pass
        print(agent_return)
