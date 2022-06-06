FROM mongo:latest
COPY data.dump /
CMD mongod --fork --logpath /var/log/mongodb.log; \
    mongorestore --db=host_nosqlforyou --gzip --archive=data.dump \
    && mongod --shutdown; \
    docker-entrypoint.sh mongod
EXPOSE 27017
