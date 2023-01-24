# README

## How to make a containr

```sh
# On Apple Silicon Mac
docker build . -t flask
docker build . --platform linux/amd64 -t flask-amd64
dodker tag flask sokoidecr.azurecr.io/flask
dodker tag flask-amd64 sokoidecr.azurecr.io/flask-amd64
az acr login --name sokoidecr
docker push sokoidecr.azurecr.io/flask-amd64

# On x64 Linux
docker build . -t flask-amd64
docker tag flask-amd64 sokoidecr.azurecr.io/flask-amd64
az acr login --name sokoidecr
docker push sokoidecr.azurecr.io/flask-amd64
```

## Prereq

* If you are pulling from sokoidecr Azure container registry into your K8s, change the flask container path to your container registry or Dockerhub
* Or, define `acr-secret` to pull from sokoidecr
* <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-kubernetes>

```
kubectl create secret docker-registry acr-secret \
    --docker-server=sokoidecr.azurecr.io \
    --docker-username=$USERNAME \
    --docker-password=$PASSWROD
```

## How to add the container in AKS

```sh
kubectl apply -f flask.yml
```

## How to test

```sh
# curl $flask-external-ip several times
curl -L 20.222.216.116/redirect
# you can see the request is round robin
k get logs -f $pod # do this for 2 pods


# curl $nginx-external-ip several times
curl -L 10.108.129.104/redirect
# you can see the request is sticky because of the default keep-alive
k get logs -f $pod # do this for 2 pods

# run curl with -H"Connection: close" which disable keep-alive
curl -L -H"Connection: close" 10.108.129.104/redirect
# you can see the request is not sticky anymore
k get logs -f $pod # do this for 2 pods
```
