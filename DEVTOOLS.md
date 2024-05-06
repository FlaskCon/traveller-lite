## Docker commands

### Build base layer
```bash
docker build -t flaskcon/base-layer:latest -f Dockerfile-base-layer .
```

### Compose
```bash
docker-compose up --build -d
```
```bash
docker-compose -f down
```