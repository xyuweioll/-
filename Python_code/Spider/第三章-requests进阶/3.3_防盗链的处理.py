# 爬取梨视频
# 注意：开着VPN运行程序会报错
# 1.拿到contId
# 2.拿到videoStatus返回json. -> srcURL
# 3.srcURL里面的内容进行修整
# 4.拿到视频的真实路径进行下载视频
import requests

url = "https://www.pearvideo.com/video_1631241"
conID = url.split("_")[1]
print(conID)
# 页面源代码和检查中的代码不一定完全相同，可能通过js脚本中途又进行的其他加载
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={conID}&mrd=0.983042177344978"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
    # 防盗链：朔源，本次请求的上一级是谁
    "Referer": "https://www.pearvideo.com/video_1631241"
}
resp = requests.get(videoStatusUrl, headers=headers, verify=False)
dict = resp.json()
srcUrl = dict['videoInfo']['videos']['srcUrl']
systemTime = dict['systemTime']
srcUrl =srcUrl.replace(systemTime, f"cont-{conID}")
print(srcUrl)

# 下载视频
with open(r"C:\Users\xianyu\Desktop\新建文件夹\a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)