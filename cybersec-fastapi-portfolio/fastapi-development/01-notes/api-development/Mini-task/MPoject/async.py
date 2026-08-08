
from rich import color
import time
import asyncio

async def endpoint(route :str)->str:
    print(f">> handling {route}")
#   sleep method
    asyncio.sleep(4)

    return(f"<< response {route}")
#endpoint(" ")


async def server():
    #run test request

    test=(
        "GET /shipment?id=1",
        "PATCH /shipment?id=4"
    )
    start=time.perf_counter()
    for route in test:
        
            result= endpoint(route)
            print(result)
        

    end=time.perf_counter()
    print(f"timme = {end-start:.2f}")

asyncio.run(
server()
)
