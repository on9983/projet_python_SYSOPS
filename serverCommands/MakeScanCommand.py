import nmap3, json, socket


class MakeScanCommand:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def startScan():
        nmap = nmap3.Nmap()
        results = nmap.scan_top_ports(socket.gethostbyname(socket.gethostname()+".local") + "/24")
        #results =nmap.nmap_os_detection("192.168.15.18/24")
        #results=nmap.nmap_list_scan("192.168.15.18/24")
        #results=nmap.nmap_subnet_scan("192.168.15.18/24")

        #print(results)
        #exit()

        m = ""
        nb_clients = 0
        dict_ip = {}
        for ip, data_ip in results.items():
            if('ports' in data_ip):
                if(data_ip['ports'] != []):

                    #print(data_ip)
                    #exit()

                    nb_ports = 0
                    nb_clients += 1
                    dict_ports = {}
                    for data_port in data_ip['ports']:

                        #print(data_port)
                        if data_port['state'] == 'open':
                            dict_ports.update({
                                data_port['portid']:{
                                    'state': data_port['state'],
                                    'reason': data_port['reason']
                                }
                            })
                            nb_ports += 1
                        
                    #exit()

                    dict_ip.update({ 
                        ip:{
                            'nb_ports': nb_ports,
                            'ports': dict_ports
                        }
                    })
        dict_ip.update({ 
            'nb_clients': nb_clients,
            'hostName': socket.gethostname(),
        })
        
        return(dict_ip)



