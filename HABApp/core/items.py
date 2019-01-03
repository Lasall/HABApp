import datetime
import logging
import typing

if typing.TYPE_CHECKING:
    pass

log = logging.getLogger('HABApp.Items')


class Item:
    def __init__(self, name: str):
        assert isinstance(name, str), type(name)

        self.name = name
        self.state = None

        self.last_change: datetime.datetime = None
        self.last_update: datetime.datetime = None

    def set_state(self, new_state):
        _now = datetime.datetime.now()
        if self.state != new_state:
            self.last_change = _now
        self.last_update = _now
        self.state = new_state


class Items:
    def __init__(self):
        self.items = {}  # type: typing.Dict[str,Item]

    def item_exists(self, name) -> bool:
        return name in self.items

    def get_items(self) -> list:
        return list(self.items.keys())

    def set_state(self, name, new_state):
        try:
            self.items[name].set_state(new_state)
        except KeyError:
            item = Item(name)
            item.set_state(new_state)
            self.items[name] = item

    def get_item(self, name) -> Item:
        return self.items[name]

    def pop_item(self, name) -> Item:
        return self.items.pop(name)
