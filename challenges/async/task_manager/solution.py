import asyncio

class AsyncTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Your code here
        # Hint: Append the task to self.tasks and return the task
        pass

    def cancel_task(self, task):
        # Your code here
        # Hint: Cancel the task and remove it from self.tasks
        pass

    async def get_results(self):
        results = []
        # Your code here
        # Hint: Iterate through self.tasks
        # Use await task to get the result and append it to results
        # Handle asyncio.CancelledError for canceled tasks
        return results
