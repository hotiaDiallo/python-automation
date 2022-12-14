# Python automation for devops engineer 

## [EC2 instances status checker](https://github.com/hotiaDiallo/python-automation/blob/main/ec2-status-checker.py)

## [Add Environment tags on EC2 instances](https://github.com/hotiaDiallo/python-automation/blob/main/add-enviroment-tags.py)

## [EKS clusters status checker](https://github.com/hotiaDiallo/python-automation/blob/main/eks-status-checker.py)

## [Automate volumes backups for EC2 instances](https://github.com/hotiaDiallo/python-automation/blob/main/ec2-volume-snapshot-creator.py)
- Create Snapshots of volumes for a specific EC2 instances (like Prod server) every day at 06:00
## [Automate cleaning volumes snapshots](https://github.com/hotiaDiallo/python-automation/blob/main/cleanup-old-snapshot.py)
- clean up the oldest volumes snapshots
## [Restore volume from a snapshots](https://github.com/hotiaDiallo/python-automation/blob/main/restore-volume-from-backup.py)
- restore volume from last created snapshot and attached it to a EC2 instance
## [Monitor website runnin as docker container](https://github.com/hotiaDiallo/python-automation/blob/main/monitor-website.py)
- We are going to create a Linode machine 
- Install docker on Linode ([Link to install docker](https://docs.docker.com/engine/install/debian/))
- Run a nginx container 
```commandline
docker run -d -p 8080:80 nginx
```
- monitor the application
