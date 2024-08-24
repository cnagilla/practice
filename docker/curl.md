<pre>
# Use the lightweight Alpine Linux image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Set the default command to run curl
CMD ["curl", "--version"]
</pre>

<pre>
apiVersion: v1
kind: Pod
metadata:
  name: curl-pod
spec:
  containers:
  - name: curl-container
    image: my-curl-image
    command: ["sleep", "infinity"]
</pre>