import signal


class GracefulShutdown:
    shutdown_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, *args):
        self.shutdown_now = True
