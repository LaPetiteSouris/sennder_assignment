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

```shell
docker-compose build

docker-compose up

```
The API is available on `localhost:8000` (depending on your docker-compose network)

## Tests

General test strategies are:

1. Test fetching raw data from external API
2. Test logics to parse raw data to results correctly
3. Test calling the API endpoints directly

To execute test suits, either use the dedicated Docker container

```shell
docker build . -f Dockerfile_test -t sennder_test

docker run sennder_test
```
Or install dependencies to execute the test in your virtual environment

```shell
pip3 install -r requirements.txt
pip3 install -r requirements-test.txt


pytest -v 
```
**NOTE**:  During the test execution, the programm will hit external API. Hitting external API everytime for test is considered to be a bad practice as:
- Increase execution time
- Increase network IO
- Make the test's behavior non-deterministic and flaky

Also, mocking external API is considered a bad practice as well:
- We should not mock what we do not own
- It makes our tests to depend a lot of hypothesis.
- Evolvement is difficult

Thus, the package `vcrpy` is usded. This package record the reply of external API and replay it for future execution. You may notice tht a folder named `tests\__fixtures__` is created .after first execution of the tests. The next execution is not going to hit external API any more, but relies on these fixtures to execute the test.

To explicitly invalidate the fixtures, just delete this folder and the next execution will create new fixtures based on actual data coming from external services.

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
