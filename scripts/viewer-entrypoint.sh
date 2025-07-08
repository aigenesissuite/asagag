#!/bin/sh
set -e

echo "Starting Typebot Viewer..."

# Database migrations
if [ "$SKIP_MIGRATIONS" != "true" ]; then
  echo "Running database migrations..."
  ./node_modules/.bin/prisma migrate deploy --schema=packages/prisma/postgresql/schema.prisma || true
fi

# Start the viewer
cd apps/viewer
exec node server.js
