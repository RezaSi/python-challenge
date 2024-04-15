import os
import sys
import unittest
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from solution import AsyncTaskManager

async def mock_task(value):
    await asyncio.sleep(1)
    return value * 2

class TestAsyncTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = AsyncTaskManager()

    def test_add_tasks(self):
        tasks = [mock_task(i) for i in range(1, 6)]
        for task in tasks:
            self.task_manager.add_task(task)
        self.assertEqual(len(self.task_manager.tasks), 5)

    def test_cancel_tasks(self):
        task1 = self.task_manager.add_task(mock_task(1))
        task2 = self.task_manager.add_task(mock_task(2))
        self.task_manager.cancel_task(task1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0], task2)

    def test_get_results(self):
        loop = asyncio.get_event_loop()
        tasks = [self.task_manager.add_task(mock_task(i)) for i in range(1, 6)]
        results = loop.run_until_complete(self.task_manager.get_results())
        self.assertEqual(len(results), 5)
        for i, result in enumerate(results, start=1):
            self.assertEqual(result, i * 2)

if __name__ == '__main__':
    unittest.main()
