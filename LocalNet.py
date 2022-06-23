class Server:
    it = iter(i for i in range(1,2**4))
    
    @classmethod
    def ip_creator(cls):
        return next(cls.it)
            
    def __init__(self):
        self.ip = self.ip_creator()
        self.to_send = list()
        self.buffer = list()

    @staticmethod    
    def send_data(data):
        router.get_data(data)
        
    def save_data(self, data):
        self.buffer.append(data)
        
    def get_ip(self):
        return self.ip
    
    def get_data(self):
        return self.buffer
        
        
class Router:
    __instance: None|object = None
    
    __buffer = []
    
    __adress_table = dict()
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance
    
    # def __init__(self):
    #     for serv in self.servers_list:
    #         self.__adress_table.fromkeys
    
    def link(self, server):
        self.__adress_table.setdefault(server.ip, server)
        
    def unlink(self, server):
        ...

    @classmethod    
    def get_data(cls, packet):
        cls.__buffer.append(packet)
    
    @classmethod
    def clear_buffer(cls):
        cls.__buffer.clear()
        
    @classmethod
    def send_data(cls):
        for pack in cls.__buffer:
            ip_dest = pack.ip_dest
            for ip, server in cls.__adress_table.items():
                if ip == ip_dest:
                    server.save_data(pack)
        cls.clear_buffer()
        
    
class Data:
    def __init__(self, data:str, ip:int):
        self.data = data
        self.ip_dest = ip
    
    
router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from[0].data)
print(msg_lst_to[0].data)
