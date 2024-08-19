# from lagent.actions import ActionExecutor, BingBrowser
# from lagent.llms import INTERNLM2_META, LMDeployServer, LMDeployClient, HFTransformerCasualLM,GPTAPI
# from openai import OpenAI

class A:
    func_list = []
    def foo(self, a):
        def calc():
            print(a*2)
        self.func_list.append(calc)


if __name__ == "__main__" :
    a = A()
    a.foo(10)
    
    for o in a.func_list:
        o()