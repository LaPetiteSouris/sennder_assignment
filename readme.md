## Execution and Deployment

The project is delivered in containerized package with Docker.

For deployment, build and push your image to Kubernetes.
```
docker build . -t sennder
```
Keep in mind the environment variables that have to be set

```
    # if CACHE is not set to `REDIS`, in memory cache will be used, which is suitable only for DEV purpose
    - CACHE="REDIS"
    - CACHE_REDIS_HOST=<redis_host>
    - CACHE_REDIS_PORT=<redis_port>
    - CACHE_REDIS_PASSWORD=<redis_password>
    - STUDIO_URL="https://ghibliapi.herokuapp.com"
    - MOVIE_URL="/films"
    - PEOPLE_URL="/people"

```

If you just want to test locally, the please use `docker-compose`.

Make sure `docker-compose` is available

```
docker-compose -v
```

Then, in the root directory of the project, execute:

```
docker-compose build

docker-compose up

```
Then the API is available on `localhost:8000` (depending on your docker-compose network)

## API Contract
### Movies 
* Movies object
```
{
    id: string,
    title: string,
    description: string,
    director: string,
    producer: string,
    release_date: string,
    rt_score: string,
    people_involved: {
        id(string): {
            "id": string,
            name: string,
        }
}

```

**GET /ping**
----
  Handshake API
* **URL Params**  
  None
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
  response: pong
}
```

**GET /movies**
----
  Returns all movies in the Ghibli Studio system, matched with involved people
* **URL Params**  
  None
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
# Each movie is stored separately, with key is the movie ID

{
  movie_id: {<movie_object>}
}
```
* **Error Response:**  
  * **Code:** 501  
  **Content:** `{ error : "An error occurs upon fetching data from external service" }` 
