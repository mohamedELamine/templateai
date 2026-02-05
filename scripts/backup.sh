#!/bin/bash

BACKUP_DIR="/opt/templateai/backups"
mkdir -p $BACKUP_DIR

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Backup database
docker-compose exec -T postgres pg_dump -U templateai_user templateai_db > "$BACKUP_DIR/backup_$TIMESTAMP.sql"

# Backup templates
tar -czf "$BACKUP_DIR/templates_$TIMESTAMP.tar.gz" /opt/templateai/data/templates/

# Keep only last 30 days
find $BACKUP_DIR -name "backup_*.sql" -mtime +30 -delete
find $BACKUP_DIR -name "templates_*.tar.gz" -mtime +30 -delete

echo "Backup completed: $TIMESTAMP"
