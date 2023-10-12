import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()

loop = asyncio.get_event_loop()
loop.create_task(say('first hello', 2)) # 2초 뒤 프린트
loop.create_task(say('second hello', 1)) # 다함께 초가 지남
loop.create_task(say('third hello', 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()