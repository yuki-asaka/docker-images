# FastAPI sample

## build

```
docker build -f docker/Dockerfile -t fast-api-sample_app .
```

## poetry

```
$ docker run -it --rm  \
-v $(pwd)/:/root \
-t fast-api-sample_app /bin/bash

$ cd /root
$POETRY_HOME/bin/poetry add module
```

## tests

```
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.test.yml up test
```

## run

```
docker-compose -f docker/docker-compose.yml up app
```
