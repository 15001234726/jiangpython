from urllib import request
import chardet

if __name__ == "__main__":
    # response = request.urlopen("http://fanyi.baidu.com/")
    # html = response.read()
    # charset = chardet.detect(html)
    # html = html.decode(charset.get("encoding",1))
    # print(charset.get("encoding",1))
    # print(html)

    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    # html = response.read()
    # charset = chardet.detect(html)
    # html = html.decode(charset.get("encoding",1))
    # print(html)
    print(response.info)
    print(response.geturl())
    print(response.getcode())