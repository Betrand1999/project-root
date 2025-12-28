version https://git-lfs.github.com/spec/v1
oid sha256:394e615b3896176f1cf9c740125d5ded5ed4f97df135f1276942e915f84bdbc9
size 2771
###
k8s dashbaord URL = https://52.202.148.136:32452/#/login
###
To login K8S dashboard on the k8s cluster run =  kubectl create token dashboard-admin -n dev
####
Argo UI login URL = https://52.202.148.136:32200/login

### if pod Evicted ###
kubectl scale deployment my-app -n prod --replicas=1

kubectl delete pod -n prod --field-selector=status.phase=Failed
