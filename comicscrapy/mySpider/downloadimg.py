import requests
 
 
def download_img(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    r = requests.get(img_url, headers=headers, stream=True)
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        # 截取图片文件名
        img_name = img_url.split('/').pop()
        with open(img_name, 'wb') as f:
            f.write(r.content)
        return True
 
 
if __name__ == '__main__':
    # 下载要的图片
    img_url = "http://www.py3study.com/Public/images/article/thumb/random/48.jpg"
    ret = download_img(img_url)
    if not ret:
        print("下载失败")
    print("下载成功")

