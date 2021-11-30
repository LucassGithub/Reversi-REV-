from abc import ABC
from queue import Queue
from typing import Dict, Callable, Any


class BasePageController(ABC):
    def __init__(self) -> None:
        """
        PageController containing functions and attributes that all page controllers should have.
        Contains internals for queueing tasks and executing them, making interface to other page
        controllers as simple as possible.
        """
        self._queue: Queue = Queue()
        self._task_execute_dict: Dict[str, Callable[..., None]] = {}

    def run(self) -> None:
        """
        Waits for task to be queued then executes that task
        """
        next_task: str
        next_task_info: Any
        # Get task from queue
        next_task, next_task_info = self._queue.get()
        # Execute task if known
        if next_task in self._task_execute_dict:
            # do we need this if/else statement here? Couldn't it just be:
            # self._task_execute_dict[next_task](next_task_info)?
            if next_task_info is None:
                self._task_execute_dict[next_task]()
                # I think this should also delete the empty task right?
                # so I think we should also add:
                # del self._task_execute_dict[next_task]
            else:
                self._task_execute_dict[next_task](next_task_info)
                # I think we should also add:
                # del self._task_execute_dict[next_task](next_task_info)

    def queue(self, task_name: str, task_info: Any = None) -> None:
        """
                Queue tasks in the correct format so child classes don't need to know that format
        <<<<<<< HEAD
        =======

        >>>>>>> 5152c868477c0d6489b734af86870145d2614011
                :param task_name: Name of the task
                :param task_info: Additional info associated with the task, as 1 data type
        """
        self._queue.put((task_name, task_info))
