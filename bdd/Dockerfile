FROM mysql

COPY /bdd/SQL/init_bdd.sql /data/epcis_schema.sql
WORKDIR /data


# commande a executer au lancement du container 
CMD mysql -u $MYSQL_USER -p $MYSQL_PASSWORD < /data/init_bdd.sql 