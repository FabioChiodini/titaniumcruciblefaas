# titaniumcruciblefaas
Serverless version for titaniumcrucible

# Prerequisites

1. riff is deployed
2. the `riff` CLI is on your PATH
3. the python3 invoker is installed

    riff invokers apply -f https://github.com/projectriff/python3-function-invoker/raw/master/python3-invoker.yaml

4. the working directory is where `.py` is

# Create the function

```
riff create python3 --push
```

# Publish a message and wait for a reply

```
riff publish -i titaniumcruciblefaas --content-type=application/json -d'{"He":"llo","Wor":"ld"}' -r
```

# Delete the function and its input topic

```
riff delete --all
```

# NOTES
Use
watch -n 1 kubectl get pods
