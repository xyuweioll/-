import time
import asyncio

# async def func1():
#     print('你好，我是大帅哥1')
#     # time.sleep(3)   # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码
#     print('你好，我是你爸爸1')
#
#
# async def func2():
#     print('你好，我是大帅哥2')
#     # time.sleep(2)
#     await asyncio.sleep(2)  # 异步操作的代码
#     print('你好，我是你爸爸2')
#
#
# async def func3():
#     print('你好，我是大帅哥3')
#     # time.sleep(4)
#     await asyncio.sleep(3)  # 异步操作的代码
#     print('你好，我是你爸爸3')
#
#
# if __name__ == '__main__':
#     f1 = func1()  # 此时的函数是异步协程函数.此时函数执行得到的是一个协程对象
#     f2 = func2()
#     f3 = func3()
#     task = [
#         f1, f2, f3
#     ]
#     t1 = time.time()
#     # 一次性启动多个任务(协程)
#     asyncio.run(asyncio.wait(task))
#     t2 = time.time()
#     print(t2-t1)

# input() 也会让程序处于阻塞状态
# requests.get(bilibili)  在网络请求返回数据之前，程序也是处于阻塞状态
# 一般情况下，当程序处于IO操作的时候，线程都会处于阻塞状态


# 协程：当程序遇见IO操作的时候。可以选择性的切换到其他任务上。
# 在微观上是一个任务一个任务的进行切换.切换条件一般就是IO操作
# 在宏观上，我们能看到的是多个任务一起在执行
# 多任务异步操作
# 上方所讲的一切都是在单线程的条件下

# ================================================================
# 在爬虫邻域的应用
import requests


async def download(url):
    print(f'准备开始下载:{url}')
    await asyncio.sleep(2)   # 网络请求
    print("下载完成")


async def main():
    urls = [
        "http://www.baidu.com"
        "http://www.bilibili.com"
        "http://www.163.com"
    ]

    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())