from datetime import datetime

dtime_now: datetime.now = datetime.now()


async def minutely_do(*functions):
    global dtime_now

    if datetime.now().minute > dtime_now.minute:
        dtime_now = datetime.now()

        for function, parameter in functions:
            await function(embed=parameter)
