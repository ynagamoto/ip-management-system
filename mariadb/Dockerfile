FROM mariadb:latest
COPY ./docker-entrypoint.sh /
COPY ./init-sql/init.sql /docker-entrypoint-initdb.d
CMD ["mysqld"]
