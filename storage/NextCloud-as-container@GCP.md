# installing NextCloud container to GCP GKE




Preparations
```shell
gcloud ini
gcloud config set accessibility/screen_reader false
gcloud auth list
gcloud config list project
gcloud config set compute/region europe-north1
gcloud config set compute/zone europe-north1-c
gcloud config set project spry-analyzer-xxxxxx
```



## Create DB, DB user in Cloud SQL:
```
34.88.xx.xx
172.21.xx.xx
DB: hub2_2dz_fi_nextcloud
u: hub2_2dz_fi_nextcloud
p: (StrongPass)
```



## Create repostory in Artifact Registry
```
Docker
Remote
Docker Hub
Unauthenticated
```



Create, check
```bash
gcloud artifacts repositories create nc-docker-local \
   --repository-format=docker \
   --mode=standard-repository \
   --location=europe-north1
gcloud artifacts repositories list
```


Get URL for repository
```bash
gcloud artifacts repositories describe nc-docker-local --location=europe-north1
```


Make local tmp dir, clone repo
```bash
mkdir delme11
cd delme11/docker
git clone https://github.com/nextcloud/docker.git
```

Copy templates
```bash
cp .examples/dockerfiles/full/apache/Dockerfile .
cp .examples/dockerfiles/full/apache/supervisord.conf .
cp .examples/docker-compose/insecure/mariadb/apache/db.env .
```

Provide ecredentials
```bash
vi db.env
cp .examples/docker-compose/insecure/mariadb/apache/docker-compose.yml .
vi docker-compose.yml
```

Build application, tag it and push it to repository
```bash
docker build -t europe-north1-docker.pkg.dev/spry-analyzer-xxxxxx/nc-docker-local/nc-docker-app:v1 .
docker images
```

Give permissions. Get project iD number.
```bash
gcloud projects list
853xxxxxxx034

gcloud artifacts repositories add-iam-policy-binding nc-docker-local \
    --location=europe-north1 \
    --member=serviceAccount:853xxxxxxx34-compute@developer.gserviceaccount.com \
    --role="roles/artifactregistry.reader"

gcloud artifacts repositories add-iam-policy-binding nc-docker-local \
    --location=europe-north1 \
    --member=serviceAccount:853xxxxxxx34-compute@developer.gserviceaccount.com \
    --role="roles/artifactregistry.writer"
```

Issue:
```bash
ERROR: (gcloud.artifacts.repositories.add-iam-policy-binding) PERMISSION_DENIED: The caller does not have permission
```


Run docker locally (will be exposed to 8080)
```bash
docker run --rm -p 8080:80 europe-north1-docker.pkg.dev/spry-analyzer-xxxxxx/nc-docker-local/nc-docker-app:v1
```



Pushing docker image into Artifact Registry
```bash
gcloud auth configure-docker europe-north1-docker.pkg.dev
docker push europe-north1-docker.pkg.dev/spry-analyzer-xxxxxx/nc-docker-local/nc-docker-app:v1
```


List content of repostiory
```bash
gcloud artifacts files list --location=europe-north1 --project=spry-analyzer-xxxxxx --repository=nc-docker-local
```


Create a GKE cluster
```shell
gcloud components install kubectl
gcloud container clusters create --machine-type=e2-micro --zone=europe-north1-c twodz-nc-demo
gcloud container clusters list
```


Get authentication credentials for the cluster (in order to manage it)
```shell
gcloud container clusters get-credentials twodz-nc-demo --zone=europe-north1-c
kubectl cluster-info
```



Deploy an application to the cluster
```shell
kubectl create deployment nc-demo-app --image=europe-north1-docker.pkg.dev/spry-analyzer-xxxxxx/nc-docker-local/nc-docker-app:v3
kubectl get deployments
kubectl scale deployment nc-demo-app --replicas=1
kubectl autoscale deployment nc-demo-app --cpu-percent=80 --min=1 --max=1
kubectl get pods --output=wide
kubectl exec --stdin --tty nc-demo-app-54dc479f5-crvhx -- /bin/bash
```



## Publish to Internet (create load balancer)
```bash
kubectl expose deployment nc-demo-app --name=nc-demo-app-service --type=LoadBalancer --port 80 --target-port 80
# wait for external IP be assigned from '<pending> state'
kubectl get services --output=wide
firefox http://[EXTERNAL-IP]:80
```



## Cleaning
```shell
kubectl delete  deployment nc-demo-app
gcloud container clusters delete twodz-nc-demo --zone=europe-north1-c
docker rmi -f 0fa923cc879e
```






Issue:
```
Memory limit of 512 MiB exceeded with 512 MiB used. Consider increasing the memory limit, see https://cloud.google.com/run/docs/configuring/memory-limits
```
Solution: increase RAM size.





Create Volume in Cloud Storage (Bucket).








troubleshooting
```bash
kubectl get pods --output=wide
kubectl exec --stdin --tty nc-demo-app-54dc479f5-crvhx -- /bin/bash
apt update
apt install net-tools
netstat -ntap
```
