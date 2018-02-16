CONNECT_TIMEOUT = 65
READ_TIMEOUT = 65

class Contrived:
    is_contrived = True

    def __init__(self, contrived):
        self.is_contrived = contrived

def configure_params(name):
    return "something " + name