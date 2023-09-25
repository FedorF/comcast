from abc import ABC, abstractmethod


class BaseUI(ABC):
    @abstractmethod
    def plot_red_signal(self):
        raise NotImplementedError("plot_red_signal() method must be implemented")

    def plot_orange_signal(self):
        raise NotImplementedError("plot_red_signal() method must be implemented")

    def plot_green_signal(self):
        raise NotImplementedError("plot_red_signal() method must be implemented")

    def plot_blank(self):
        raise NotImplementedError("plot_red_signal() method must be implemented")


class UI(BaseUI):
    def plot_red_signal(self):
        print(r'''                      _[]_
                     [____]
                 .----'  '----.
             .===|    .==.    |===.
             \   |   /####\   |   /
             /   |   \####/   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
                 '--.______.--'
        ''')

    def plot_orange_signal(self):
        print(r'''                      _[]_
                     [____]
                 .----'  '----.
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /####\   |   /
             /   |   \####/   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
                 '--.______.--'
        ''')


    def plot_green_signal(self):
        print(r'''                      _[]_
                     [____]
                 .----'  '----.
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /####\   |   /
             /   |   \####/   |   \
             '===|    `""`    |==='
                 '--.______.--'
        ''')

    def plot_blank(self):
        print(r'''                      _[]_
                     [____]
                 .----'  '----.
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
             .===|    .==.    |===.
             \   |   /    \   |   /
             /   |   \    /   |   \
             '===|    `""`    |==='
                 '--.______.--'
        ''')
