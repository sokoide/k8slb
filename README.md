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
dodker tag flask-amd64 sokoidecr.azurecr.io/flask-amd64
az acr login --name sokoidecr
docker push sokoidecr.azurecr.io/flask-amd64
```

## How to add the container in AKS

```sh
kubectl apply -f flask.yml
```

## How to test

```sh
curl -L 20.222.216.116

curl -L 20.222.216.116/redirect
k get logs -f $pod # do this for 2 pods
```
