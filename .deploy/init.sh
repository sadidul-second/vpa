#!/bin/bash

#ssh root@185.32.161.60 -p 42404 -i ~/.ssh/id_ed25519

PUBLIC_IP=185.32.161.60
PORT=42404
REMOTE_DESTINATION=/root/
SSH_KEY=~/runpodio

ssh root@${PUBLIC_IP} -p ${PORT} -i ${SSH_KEY} -t 'mkdir -p uploads/'
scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}.env root@${PUBLIC_IP}:${REMOTE_DESTINATION}

scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}*.py root@${PUBLIC_IP}:${REMOTE_DESTINATION}
#scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}example.env root@${PUBLIC_IP}:${REMOTE_DESTINATION}
scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}requirements.txt root@${PUBLIC_IP}:${REMOTE_DESTINATION}
scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}Dockerfile root@${PUBLIC_IP}:${REMOTE_DESTINATION}
scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}docker-compose.yml root@${PUBLIC_IP}:${REMOTE_DESTINATION}
scp -i ${SSH_KEY} -P ${PORT} ${SOURCE_ROOT}nginx.conf root@${PUBLIC_IP}:${REMOTE_DESTINATION}

scp -i ${SSH_KEY} -P ${PORT} uploads/* root@${PUBLIC_IP}:${REMOTE_DESTINATION}/uploads/


