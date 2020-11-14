# ReX
Self-contained automated network and server healing service.

## Summary
ReX is a completely self-contained service that can perform rescue operations on critical infrastructure such as restarting and migrating VMs and containers.

## Installing
```
apt-get install python3 python3-pip git -y
cd /opt
git clone https://github.com/ARMmaster17/ReX.git
cd ./ReX
pip install -r requirements.txt
cp ./rex.service /etc/systemd/system/rex.service
sudo systemctl daemon-reload
sudo systemctl enable rex
nano ./promxox.yml
```

Fill in `proxmox.yml` with the connection details for your Proxmox cluster.

```
sudo systemctl start rex
```

## Integration
// TODO: Zabbix script

## Features in progress
- Checks if rescue operations worked.
- YAML configurable sequence of operations.
- AIO bash script to install.
- Support for hypervisors other than Proxmox.
- Network topology mapping for tracing source of network outages.

For a list of all features to be added see the **Issues** tab.

# License
MIT