# -*- coding: utf-8 -*-

from pixivpy3 import *
import asyncio

try:
    import ujson
except:
    import json as ujson

import aiofiles
import os
import imageDownload

_USERNAME = ""
_PASSWORD = ""
_ID = 28246124
_NUMBER = 'all'


async def writeJson(p, info):
    async with aiofiles.open(p, 'w', encoding='utf-8') as f:
        await f.write(ujson.dumps(info))


async def main():

    # login
    api = ByPassSniApi()
    api.require_appapi_hosts()
    api.set_accept_language('zh-cn')
    api.login(_USERNAME, _PASSWORD)

    # get all
    id = int(_ID)
    result = {
        "data": [],
        "number": 0,
        "next_url": []
    }
    offset = 0
    mark = True
    while mark:
        json_result = api.user_illusts(id, offset = offset)
        result['data'] += json_result['illusts']
        result['number'] += 1
        if json_result['next_url'] == None:
            mark = False
        result['next_url'].append(json_result['next_url'])
        # print(json_result['next_url'])
        offset += 30
    
    # sort out
    newResult = {
        "data": [],
        "number": 0,
        "count": 0
    }
    for i in result['data']:
        newStructure = {
            'id': i['id'],
            'count': i['page_count'],
            'url': [],
            'url_large': [],
            'cat_url': [],
            'cat_url_large': []
        }
        newStructure['count'] = i['page_count']
        newStructure['id'] = i['id']
        # url
        if 'original_image_url' in i['meta_single_page']:
            newStructure['url'].append(i['meta_single_page']['original_image_url'])
            newStructure['url_large'].append(i['image_urls']['large'])
        else:
            for j in i['meta_pages']:
                newStructure['url'].append(j['image_urls']['original'])
                newStructure['url_large'].append(j['image_urls']['large'])
        # cat_url
        for j in newStructure['url']:
            newStructure['cat_url'].append(j.replace('i.pximg.net', 'i.pixiv.cat'))
        for j in newStructure['url_large']:
            newStructure['cat_url_large'].append(j.replace('i.pximg.net', 'i.pixiv.cat'))
        newResult['data'].append(newStructure)
        newResult['number'] += 1
        newResult['count'] += newStructure['count']
    
        # Write file
        await writeJson(str(_ID) + '.json', newResult)

        await download(quantity = _NUMBER)

async def readJson(p):
    if not os.path.exists(p):
        raise IOError
    async with aiofiles.open(p, 'r', encoding='utf-8') as f:
        content = await f.read()
    content = ujson.loads(content)
    return content


async def download(quantity = 10):
    fileName = str(_ID) + '.json'
    content = await readJson(fileName)
    if quantity == 'all':
        quantity = content['count']
    elif quantity > content['count']:
        quantity = content['count']
    list = await extractNewList(content, quantity)
    print(len(list))
    await imageDownload.main(list, _ID)


async def extractNewList(content, quantity):
    count = 0
    result = []
    for i in content['data']:
        for j in i['cat_url']:
            result.append(j)
            count += 1
            if count == quantity:
                return result


if __name__ == "__main__":
    asyncio.run(main())
    


        
