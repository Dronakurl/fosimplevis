# Fiftyone needs a database

export FIFTYONE_DATABASE_URI=mongodb://localhost:27017

# Prune stopped containers
docker container prune -f

# Check if the mongodb container is already running
if [ "$(docker ps -q -f name=mongodb)" ]; then
  echo "Container 'mongodb' is already running."
else
  # Run a new MongoDB container if it's not already running
  docker run -d --name mongodb -p 27017:27017 mongo
fi

uv run python start.py
