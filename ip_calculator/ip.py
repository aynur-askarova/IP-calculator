ip=input('Input ip:')
ip=ip.split('.')
a=int(ip[0])
b=int(ip[1])
c=int(ip[2])
d=int(ip[3])
l=['']
l+=[a]
l+=[b]
l+=[c]
l+=[d]
netmask=int(input('Number:'))
Subnet_mask='255.'*(netmask//8)+str(2**8-1-(2**(8-netmask%8)-1))+'.0'*(4-netmask//8-1)
print('Subnet_mask:'+Subnet_mask)
Count_of_host_bits=32-netmask
Hosts_Net=(2**Count_of_host_bits)-2
print('Count of host bits:',Count_of_host_bits)
print('Hosts/Net:',Hosts_Net)
x=255-(2**8-1-(2**(8-netmask%8)-1))
nw_count=netmask//8
nw_part=''
i=x
k=0
while l[nw_count+1]>i:
    k+=(x+1)
    i+=(x+1)
for j in range(1,nw_count+1):
    nw_part+=str(l[j])+'.'
Network=nw_part+str(k)+'.0'*(4-netmask//8-1)
print('Count of networks:',2**nw_count)
print('Network:',Network)
Broadcast=nw_part+str(i)+'.255'*(4-netmask//8-1)
print('Broadcast:'+Broadcast)
l_n=len(Network)
l_b=len(Broadcast)
Host_min=Network[0:l_n-1]
Host_min+=str(int(Network[l_n-1])+1)
print('Host_min:'+Host_min)
Host_max=Broadcast[0:l_b-1]
Host_max+=str(int(Broadcast[l_b-1])-1)
print('Host_max:'+Host_max)