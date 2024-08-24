### Helm Install
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
sudo snap install helm --classic


source <(helm completion bash)
helm completion bash > /etc/bash_completion.d/helm

source <(kubectl completion bash)
echo "source <(kubectl completion bash)" >> ~/.bashrc 

### Springboot
rahulwagh17/kubernetes:jhooq-k8s-springboot
port 8080
helm template springboot
helm lint springboot
helm install springboot --debug --dry-run springboot
helm install myfirstspringboot springboot

export POD_NAME=$(kubectl get pods --namespace {{ .Release.Namespace }} -l "app.kubernetes.io/name={{ include "springboot.name" . }},app.kubernetes.io/instance={{ .Release.Name }}" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace {{ .Release.Namespace }} $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080 to use your application"

forward traffic from local to removte pod
kubectl --namespace {{ .Release.Namespace }} port-forward $POD_NAME 8080:$CONTAINER_PORT
curl 10.233.28.240:8080/hello


### bitnami/redis
kubectl run curlpod --image=curlimages/curl --restart=Never -- sleep 3600
kubectl get pods
kubectl exec -it curlpod -- sh
curl http://10.0.0.1
kubectl delete pod curlpod

kubectl run mycurlpod --image=curlimages/curl -i --tty -- sh
Ctl+d
curl http://10.0.0.1



### Error with service
helm -n demo install myhelloworld helloworld
Error: INSTALLATION FAILED: 1 error occurred:
        * admission webhook "validation.gatekeeper.sh" denied the request: [azurepolicy-k8sazurev1loadbalancernopublic-ab1228302ee5062f4baa] Load Balancers should not have public IPs. azure-load-balancer-internal annotation is required for myhelloworld


### Plugins
