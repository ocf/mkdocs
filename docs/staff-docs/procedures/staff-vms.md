# Staff VMs

[Helpful Redhat Docs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-starting_suspending_resuming_saving_and_restoring_a_guest_virtual_machine-starting_a_defined_domain#sect-start-vm)


List current VMs: `sudo virsh list —all`

List current zfs: `zfs list`

Start a shut off VM up again: `sudo virsh start VMNAME`

Access VM: `sudo virsh console VMNAME`


Destroy:

`sudo virsh destroy VMNAME`

`sudo virsh undefine --nvram VMNAME`

## Creating new Staff VMs


 1. SSH into cloudsdale
 2. Create a new zfs dataset for USERNAME (requires root)

    `sudo zfs create staffvm/USERNAME -o mountpoint=/staffvm/USERNAME`
 3. Create the VM named VMNAME (natural disaster themed). iso is in 

    `sudo virt-install --name VMNAME --memory 2048 --cpu host --vcpus 1 --disk size=5 --boot uefi --graphics none --cdrom debian-12.9.0-amd64-netinst.iso --osinfo detect=on,name=debian11`
 4. Press 'e' on the Install option
 5. add the argument `console=ttyS0` to the linux line

    
    1. `/install.amd/vmlinuz console=ttyS0`
 6. Set IP to new ip from Staff VM Allocations Spreadsheet

    
    1. take the ip of an unused/no longer exists staff vm lol
 7. Netmask is default
 8. Name server address: `169.229.226.22`
 9. hostname same as vmname
10. domain name: ocf.berkeley.edu
11. pick the user's password
12. do default disk partitioning
13. Say no
14. set ocf for mirrors
15. no proxy
16. [add DNS](https://docs.ocf.berkeley.edu/doc/updating-dns-records-OXi75lHJHb)


\