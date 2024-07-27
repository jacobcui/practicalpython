import nmap

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sS -sV')
    
    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print(f'State: {nm[host].state()}')
        
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            lport = nm[host][proto].keys()
            for port in lport:
                print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')

# Example usage
scan_network('192.168.166.0/24')
