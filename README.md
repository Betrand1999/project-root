sudo systemctl restart sshd
3.235.142.37:8443 # rancher 

sudo docker run --privileged -d \
  --restart=always \
  -p 8081:80 -p 8443:443 \
  rancher/rancher

# docker volume prune -f


/etc/apache2/sites-available/000-default.conf
sudo systemctl restart apache2
update docker file for container port
update your python app port


# 
docker rmi -f $(docker images betrand1997/my-static-websites -q)
