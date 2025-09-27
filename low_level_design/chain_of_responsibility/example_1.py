""" Optional are discribe in my Python Code Folder. """

from abc import ABC, abstractmethod
from typing import List, Optional

class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass

class Component(ComponentWithContextualHelp):
    def __init__(self, tooltip_text: Optional[str] = None):
        self.tooltip_text = tooltip_text
        self.container: Optional["Container"] = None

    def show_help(self):
        if self.tooltip_text is not None:
            print(f"Showing tooltip: {self.tooltip_text}")
        else:
            self.container.show_help()


class Container(ComponentWithContextualHelp):
    def __init__(self, tooltip_text: Optional[str] = None):
        self.tooltip_text = tooltip_text
        self.children: List[Component] = []

    def add(self, child):
        self.children.append(child)
        child.container = self

    def show_help(self):
        if self.tooltip_text:
            print(f"Showing Tooltip : {self.tooltip_text}")

class Button(Component):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, tooltip_text:Optional[str] = None):
        super().__init__(tooltip_text)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

class Panel(Container):
    def __init__(self, x: int, y: int, width: int, height: int, modal_help_text: Optional[str] = None):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text is not None:
            print(f"Showing Modal help: {self.modal_help_text}")
        else:
            super().show_help()

class Dialog(Container):
    def __init__(self, title: str, wiki_page_url: Optional[str] = None):
        super().__init__()
        self.title = title
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print(f"Opening wiki page: {self.wiki_page_url}")
        else:
            super().show_help()


class Application:
    def __init__(self):
        self.dialog = None
        self.panel = None

    def create_ui(self):
        self.dialog = Dialog("Budget Reports", "http://aranik43.blogspot.com/")
        self.panel = Panel(0, 0, 400, 800, "This panel shows budget details.")

        ok = Button(250, 760, 50, 20, "Ok", "This is the Ok Button.")
        cancel = Button(320, 760, 50, 20, "Cancel")

        self.panel.add(ok)
        self.panel.add(cancel)
        self.dialog.add(self.panel)

    def on_f1_key_press(self, component: Component):
        component.show_help()


if __name__ == "__main__":
    app = Application()
    app.create_ui()

    print("F1 Pressed On Ok Button: ")
    app.on_f1_key_press(app.panel.children[0])

    print("F1 Pressed On Cancel Button: ")
    app.on_f1_key_press(app.panel.children[1])

