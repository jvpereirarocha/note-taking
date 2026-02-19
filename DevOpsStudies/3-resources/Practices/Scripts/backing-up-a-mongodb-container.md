To execute the backup:
```bash
echo $(kubectl get pods -n tilt | grep mongo-joaorocha* | cut -d ' ' -f1)

kubectl exec $PODNAME -n tilt -- mongodump \
--username dev \
--password coracaopeludo21 \
--authenticationDatabase admin \
--db condominio \
--archive=/tmp/db_backup.gz --gzip
```

To copy the remote file into my local machine:
```bash
echo $(kubectl get pods -n tilt | grep mongo-joaorocha* | cut -d ' ' -f1)

kubectl -n tilt cp mongo-joaorocha-655b5cbcb8-8x9xt:/tmp/db_backup.gz /tmp/db_backup.gz
```