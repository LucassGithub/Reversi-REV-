from typing import Callable

from client.controllers.base_page_controller import BasePageController
from client.views.home_button_page_view import HomeButtonPageView


class HomeButtonPageController(BasePageController):
    def __init__(
        self,
        go_home_callback: Callable[[], None],
    ) -> None:
        """
        Specific type of page controller with a home button already handled.
        Many pages could have a home button, so this removes duplicate code.

        :param go_home_callback: Callback to call when going to the home screen
        """
        super().__init__()
        self._task_execute_dict["home_button"] = self.__execute_task_home_button
        self._go_home_callback: Callable[[], None] = go_home_callback

    def handle_home_button(self) -> None:
        """
        Handles home button action from the user by queueing task
        """
        self.queue(task_name="home_button")

    def __execute_task_home_button(self) -> None:
        """
        Takes action on the home button by notifying callback
        """
        self._go_home_callback()
