def urls_from_txt(txt):
    with open(txt, "r", encoding="utf-8") as f:
        urls = f.readlines()
        print(urls)
        return urls
