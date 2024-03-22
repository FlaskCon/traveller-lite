## Docker commands

### Build base layer
```bash
docker build -t flaskcon/base-layer -f Dockerfile-base-layer .
```

### Compose
```bash
docker-compose up --build -d 
```