from lagent.actions import ActionExecutor, BingBrowser

if __name__ == "__main__" :
    bing = BingBrowser(searcher_type='DuckDuckGoSearch', topk=6, proxy = "http://10.99.93.35:8080")
    res = bing.open_url("https://zh.wikipedia.org/wiki/天津文化")
    print(res)