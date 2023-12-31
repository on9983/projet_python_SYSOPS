import socket,sys,threading,time,nmap3
from tkinter import *

# ==== Scan Vars ====
ip_s = 1
ip_f = 1024
log = []
ports = []
target = 'localhost'

# ==== Scanning Functions ====
def startScan():
	nmap = nmap3.Nmap()
	results = nmap.scan_top_ports("192.168.15.18/24")
	#print(results)
	m = ""
	nb_client = 0
	for ip, data_ip in results.items():
		if('ports' in data_ip):
			if(data_ip['ports'] != []):
				m = "Adresse IP : " + ip + "\n"
				listbox.insert("end", m)
				m = "    "+"port : "
				listbox.insert("end", m)
				nb_client += 1
				L25.config(text = nb_client)
				for port_label, port_info in data_ip['ports'][0].items():
					if (type(port_info) is str):
						m = "    " + "    " + port_label + " : " + port_info + "\n"
						listbox.insert("end", m)
						log.append(m)
						# updateResult()
	
		
def saveScan():
	global log, target, ports, ip_f
	log[5] = " Result:\t[ " + str(len(ports)) + " / " + str(ip_f) + " ]\n"
	with open('scanData.txt', mode='wt', encoding='utf-8') as myfile:
		myfile.write('\n'.join(log))

def clearScan():
	listbox.delete(0, 'end')

# ==== GUI ====
gui = Tk()
gui.title('Port Scanner')
gui.geometry("400x600+20+20")

# ==== Colors ====
m1c = '#00ee00'
bgc = '#222222'
dbg = '#000000'
fgc = '#111111'

gui.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc,activeForeground=bgc, highlightColor=m1c, highlightBackground=m1c)

# ==== Labels ====
L11 = Label(gui, text = "Seahawks Harvester",  font=("Helvetica", 16))
L11.place(x = 16, y = 10)

L21 = Label(gui, text = "Nom du harvester : ")
L21.place(x = 16, y = 90)
L22 = Label(gui, text = "???")
L22.place(x = 180, y = 90)

L23 = Label(gui, text = "IP du harvester : ")
L23.place(x = 16, y = 120)
L23 = Label(gui, text = "???")
L23.place(x = 180, y = 120)

L24 = Label(gui, text = "Nb de clients detectés : ")
L24.place(x = 16, y = 150)
L25 = Label(gui, text = "???")
L25.place(x = 180, y = 150)

L26 = Label(gui, text = "Liste des connexions LAN ")
L26.place(x = 16, y = 240)


# ==== Ports list ====
frame = Frame(gui)
frame.place(x = 16, y = 275, width = 370, height = 215)
listbox = Listbox(frame, width = 59, height = 12)
listbox.place(x = 0, y = 0)
listbox.bind('<<ListboxSelect>>')
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# ==== Buttons / Scans ====
B11 = Button(gui, text = "Start Scan", command=startScan)
B11.place(x = 16, y = 500, width = 170)
B21 = Button(gui, text = "Save Result", command=saveScan)
B21.place(x = 210, y = 500, width = 170)

# ==== Start GUI ====
gui.mainloop()