#!/bin/bash

echo "En attente de l'api..."
while  ! nc -z back 8000
do
    sleep 0.1
done

echo "API demarree"


exec "$@"