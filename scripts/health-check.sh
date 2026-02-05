#!/bin/bash

echo "Checking services health..."

services=("api-gateway:8000" "langgraph-orchestrator:8001" "autogen-agents:8002" "code-generation:8003" "testing-service:8004" "database-service:8005")

for service in "${services[@]}"; do
    IFS=':' read -r name port <<< "$service"
    if curl -f http://localhost:$port/health > /dev/null 2>&1; then
        echo "✓ $name is healthy"
    else
        echo "✗ $name is DOWN"
    fi
done
