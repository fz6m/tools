# -*- coding:utf-8 -*-

import aiohttp
import asyncio
import aiofiles
import os


async def main():
    p = './download.txt'
    out = []
    async with aiofiles.open(p, 'r', encoding='utf-8') as f:
        content = await f.readlines()
    for c in content:
        if c.strip() != '':
            out.append(c.strip())

    # print(out)

    for item in out:
        name = item[item.rfind('/') + 1:]
        img = await asyncGet(item)
        if not os.path.exists('./out'):
            os.mkdir('./out')
        await savePicture(f'./out/{name}', img)


async def savePicture(p, img):
    async with aiofiles.open(p, 'wb') as f:
        await f.write(img)


async def asyncGet(url, headers='', timeout=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            img = await res.read()
    return img


if __name__ == "__main__":
    asyncio.run(main())
