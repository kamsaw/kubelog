# debugowanie webhook kubernetes
```
student@cp$ sudo vim /etc/kubernetes/manifests/kube-apiserver.yaml
---
- --audit-log-path=/var/log/audit.log
- --audit-policy-file=/etc/kubernetes/test-audit.yaml
- --audit-webhook-config-file=/etc/kubernetes/test-audit-webhook
...
volumeMounts:
  - mountPath: /etc/kubernetes/test-audit-webhook
    name: webhook
	readOnly: true
  - mountPath: /etc/kubernetes/test-audit.yaml
    name: falco-audit
	readOnly: true
  - mountPath: /var/log/audit.log
    name: audit-log
    readOnly: false
...
volumes:
  - hostPath:
      path: /etc/kubernetes/test-audit-webhook
      type: File
    name: webhook
  - hostPath:
      path: /etc/kubernetes/test-audit.yaml
      type: File
    name: falco-audit
  - hostPath:
    path: /var/log/audit.log
    type: FileOrCreate
  name: audit-log
---
```
```
python3 -m http.server 8080
python3 server.py
```
