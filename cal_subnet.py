given_ip=input("Input the subnet cidr please \n")
def bin_to_ip(given_bin):
    ip = ''
    n = 8
    result = [given_bin[i:i+n] for i in range(0, len(given_bin), n)]
    for i in range(0,len(result)):
        r = result[i]
        r = str(int(r,2))
        ip += r 
        if i == len(result)-1:
            continue
        ip += '.'
    return ip

def cal_subnet(given_ip):
    last = int(given_ip.split('/')[1])
    octets = given_ip.split('/')[0].split('.')
    oct_string=""
    for octet in octets:
        octet= int(octet)
        oct = str(bin(octet))
        oct = oct[2:]
        while len(oct)<8:
            oct = '0' + oct
        oct_string += oct

    subnet_mask_bin = oct_string[0:last].replace('0','1')
    subnet_mask_bin += oct_string[last:].replace('1','0')

    subnet_mask = bin_to_ip(subnet_mask_bin)

    network_ip_bin = oct_string[0:last]
    network_ip_bin += oct_string[last:].replace('1','0')
    network_ip = bin_to_ip(network_ip_bin)

    broadcast_ip_bin = oct_string[0:last]
    broadcast_ip_bin += oct_string[last:].replace('0','1')
    broadcast_ip = bin_to_ip(broadcast_ip_bin)

    return network_ip, broadcast_ip, subnet_mask
network_ip, broadcast_ip, subnet_mask = cal_subnet(given_ip)
print ("##################################")
print(f'network ip is: {network_ip}')
print(f'broadcast ip is: {broadcast_ip}')
print(f'subnet mask is: {subnet_mask}')
print ("##################################")

