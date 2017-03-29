import time
from oslo_service import service as os_service

class MyServer(object):

    def __init__(self):
        self.stop_flag = False

    def start(self):
        while not self.stop_flag:
            time.sleep(1)
            print("waiting")

    def stop(self):
        self.stop_flag = True


class MyService(os_service.ServiceBase):
    
    def __init__(self):
        self.server = MyServer()

    def start(self):
        print("my_service starts")
        self.server.start()

    def wait(self):
        self.server.wait()

    def stop(self):
        print("my_service stops")
        self.server.stop()

    def reset(self):
        self.server.stop()
        self.server.wait()

if __name__ == '__main__':
    MyService().start()
