class Server:
    SERVERS = {}
    def __init__(self):
        self.ip = id(self)
        self.buffer = list()
        self.definition(self)
        #print(f'создан сервер с Id {self.ip}')

    @classmethod 
    def definition(cls, obj):
        cls.SERVERS[obj.ip] = obj
    
    def send_data(self, data):
        self.data = data.data
        ip = data.ip
        for r in Router.ROUTERS:
            if ip in Router.ROUTERS[r].r_servers.keys():
                right_router = r
        Router.ROUTERS[right_router].buffer.append(data)
        #print(f'из сервера {self.ip} отправлено в роутер', Router.ROUTERS[right_router].buffer)

    def get_data(self):
        #print(f'полученные сервером {self.ip} данные из роутера:',  self.buffer)
        for_res = self.buffer
        self.buffer = list()
        return for_res
        
    def get_ip(self):
        return self.ip


class Router: 
    ROUTERS = {}
    
    def __init__(self):
        self.buffer = list()
        self.r_servers = {}
        self.definition(self)
        
    @classmethod 
    def definition(cls, obj):
        cls.ROUTERS[id(obj)] = obj
        
    def link(self, server):
        #print(server.ip)
        self.r_servers[server.ip] = server 
        #print(self.r_servers)

    def unlink(self, server):
        key = id(server)
        if key in self.r_servers:
            self.r_servers.pop(key)
            
    def send_data(self):
        for_res = self.buffer
        self.buffer = list()
        for i in for_res:
            server_ip = i.ip
            data = i.data 
            Server.SERVERS[server_ip].buffer.append(i)
            #print(f'Отправленные данные на сервер {server_ip}', Server.SERVERS[server_ip].buffer)    
                
        
class Data: 
    def __init__(self, string, ip):
        self.data = string 
        self.ip = ip
        #print('Это данные ', self)


############################################
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
print(msg_lst_from[0].data)
msg_lst_to = sv_to.get_data()
