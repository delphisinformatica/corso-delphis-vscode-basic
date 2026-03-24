#!/bin/bash

echo "Starting Apache via apache2ctl..."

apache2ctl start || echo "WARNING: Apache failed to start. You can debug this inside VS Code."

# Execute the CMD passed by docker-compose ('sleep infinity')
echo "Handing off to CMD: $@"
exec "$@"