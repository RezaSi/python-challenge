import aiohttp
import asyncio
import time

async def async_file_download(url, file_path):
    start_time = time.time()
    # Your code here
    # Hint: Use aiohttp.ClientSession to send a GET request and download the file content
    # Write the content to the specified file path
    end_time = time.time()
    return end_time - start_time
