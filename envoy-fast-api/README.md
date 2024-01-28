envoy x fast api
================

This is a simple example of using envoy as a reverse proxy for a fast api application.

## Usage

- Start the application
```bash
docker-compose up
```

### envoy

- Open the browser at http://localhost/docs
- You should see the fast api documentation through envoy
- Open the browser at http://localhost/server_info
- You should see the envoy admin server information on same listener(not recommended for production)

### fastapi

- open the browser at http://localhost:8000/docs
- You should see the fast api documentation directly from the application
