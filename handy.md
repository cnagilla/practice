### Docker
docker login -u CNagillaGL -p token https://ghcr.io  
docker run -ti -d --name tfdocker --net=host -v '/home/gl/projects:/modules' tfdocker  
docker exec -it tfdocker bash

### Container Registry
az login
az acr login --name acrname.azurecr.io --expose-token > TOKEN_FILE
export DK_LOGIN_SERVER=$(cat TOKEN_FILE | jq -r .loginServer)  
export DK_ACCESS_TOKEN=$(cat TOKEN_FILE | jq -r .accessToken)  
docker login $DK_LOGIN_SERVER -u 00000000-0000-0000-0000-000000000000 -p $DK_ACCESS_TOKEN

# Kubectl
### Remove unwanted replicasets
```
for ns in $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'); do
  kubectl delete replicaset -n $ns $(kubectl -n $ns get replicaset -o jsonpath='{ .items[?(@.spec.replicas==0)].metadata.name }')
done
```
kubectl get rs -A | awk '$3 == 0 {print $1 " " $2}' | xargs -n 2 sh -c 'kubectl delete -n $0 rs $1'
## Remove unwanted pods from all namespaces 
### recursive | bash
```
for ns in $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'); do
  kubectl get pods -n $ns | grep -E '(Error|Evicted|ContainerStatusUnknown|Completed|CrashLoopBackOff)' | awk '{print $1}' | xargs kubectl delete pod -n $ns
done
```
kubectl get pods -A | grep -E '(Error|Evicted|ContainerStatusUnknown|Completed|CrashLoopBackOff)' | awk '{print $1 " " $2}' | xargs -n 2 sh -c 'kubectl delete -n $0 pod $1 --now'
### recursive | PowerShell
```
$namespaces = kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'
foreach ($ns in $namespaces) {
    $pods = kubectl get pods -n $ns | Select-String -Pattern 'Error|Evicted|ContainerStatusUnknown|Completed|CrashLoopBackOff'
    foreach ($pod in $pods) {
        $podName = $pod -split ' ')[0]
        kubectl delete pod -n $ns $podName
    }
}
```
kubectl get pods -o custom-columns=NAME:.metadata.name,CPU_REQUEST:.spec.containers[*].resources.requests.cpu,MEMORY_REQUEST:.spec.containers[*].resources.requests.memory -n ns

### Git hub runners
<pre>
permissions:
  id-token: write
  contents: read
  packages: read
  pull-requests: read
</pre>

## az Install
Step 1: Update package list
sudo apt-get update

Step 2: Install prerequisites
sudo apt-get install -y ca-certificates curl apt-transport-https lsb-release gnupg

Step 3: Add the Microsoft signing key
curl -sL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

Step 4: Add the Azure CLI software repository
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | sudo tee /etc/apt/sources.list.d/azure-cli.list

Step 5: Update package list again
sudo apt-get update

Step 6: Install the Azure CLI
sudo apt-get install -y azure-cli

### With apk
apk update
apk add --no-cache python3 py3-pip
pip3 install azure-cli

## AKS Cluster context merge
az login
### SandBox AKS Cluster
<pre>
az account set --subscription subid-subidin-the-format
az aks get-credentials --resource-group rg-name --name aks-name --overwrite-existing
kubelogin convert-kubeconfig -l azurecli
</pre>

## Terraform

terraform {
  plugin_cache_dir = "$HOME/.terraform.d/plugin-cache"
}

export TF_PLUGIN_CACHE_DIR="$HOME/.terraform.d/plugin-cache"

terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "path/to/my/key"
    region = "us-west-2"
  }
}

terraform {
  provider_installation {
    network_mirror {
      url = "https://my-mirror.example.com/"
    }
    direct {
      exclude = ["registry.terraform.io/hashicorp/*"]
    }
  }
}

# References
https://www.commandprompt.com/education/how-to-create-a-read-only-user-in-postgresql/
