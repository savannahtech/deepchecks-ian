# Interactions Logger
- Install latest version of  docker and docker-compose on to your local computer 
- Clone this project on your local machine 

## Project setup instruction 
### Prerequisites 
- Ensure docker is running 

### Setup Instructions
- Inside the project root, run docker compose `docker-compose up --build .`
- You can access the project at `0.0.0.0:8000`


### Using the API 
- Access API documentation at  `0.0.0.0:8000/docs`
- Upload CSV , with a metrice with interactions at `0.0.0.0/upload-interactions`
- To create a single interations at `0.0.0.0:8000/interactions`, Check documention on properties accepted 
- Check on metrics alert `0.0.0.0:8000/metrics`, To filter for specfic metric alert `0.0.0.0:8000/metrics?interaction={id}`

### Assumption on Improvements
- I added a simple background tasks to handle file upload this can be scaled to a full asychronous solution running on Redis e.t.c 
- We can add dynamic Metric variable later 
- Setup Kubernations and use helm secrets to secure ENV VARIABLES 