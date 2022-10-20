# requests.get()  # 同步的代码->异步操作    # 异步的http操作

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2022/0511/smallfba8de93defc344d96a7e7ebbe801649.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/0sgbvdpakxg.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/niepq3qxogc.jpg"
]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]  # 从右边切割1次取第0个
    async with aiohttp.ClientSession() as session:   # requests
        async with session.get(url) as resp:
            # 请求回来了，写入文件
            # 文件写出操作也可以用异步操作，可以自己去学习一个模块,aiofiles
            with open(fr"C:\Users\xianyu\Desktop\Picture\{name}", mode='wb') as f:
                f.write(await resp.content.read())   # 读取内容是异步的，需要await挂起
    print(name, "搞定")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)

if __name__ =='__main__':
    asyncio.run(main())
