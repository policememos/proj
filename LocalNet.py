class Server:
    it = iter(i for i in range(1,2**4))
    
    @classmethod
    def ip_creator(cls):
        return next(cls.it)
            
    def __init__(self):
        self.ip = self.ip_creator()
        self.to_send = list()
        self.buffer = list()
        
    def send_data(self, data):
        ...
        
    def get_data(self, data):
        ...
        
    def get_ip(self):
        return self.ip
        
        
class Router:
    __instance: None|object = None
    
    __buffer = []
    
    servers_list = []
    
    __adress_table = dict()
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance
    
    def __init__(self):
        for serv in self.servers_list:
            self.__adress_table.fromkeys
    
    def link(self, server):
        ...
        
    def unlink(self, server):
        ...
    
    @staticmethod
    def send_data(data):
        ...
        
    
class Data:
    def __init__(self, data:str, ip:int):
        self.data = data
        self.ip_dest = ip
    
    
    
sv = Server()
print(f'{sv.ip=}')
sv2 = Server()
print(f'{sv2.ip=}')
sv3 = Server()
print(f'{sv3.ip=}')

rt = Router()
rt.servers_list = [sv,sv2,sv3]

data = Data(строка с данными, IP-адрес назначения)

