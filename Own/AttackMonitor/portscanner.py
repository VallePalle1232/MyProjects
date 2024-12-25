import nmap


nm = nmap.PortScanner()


test_target_ip = "45.33.32.156" #Ip for nmap test site
#sV version control
#sC standard scan

arguments = "-Sv -sC scan_results" 

nm.scan(test_target_ip , arguments)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    for protocol in nm[host].all_protocols():
        print("Protocol: %s (%s)" % protocol) 