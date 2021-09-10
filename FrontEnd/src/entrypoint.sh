#!/bin/bash

echo "Waiting for the API..."
while  ! nc -z back 8000
do
    sleep 0.1
done

echo "API Started"


exec "$@"