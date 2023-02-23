## Assumptions and constraints
- Any special libraries for text processing were not used.
<<<<<<< HEAD
- Each function count words and characters only with English characters.
=======
- Each function count words and characters only with English characters. 
>>>>>>> e794c4fd59c0bb669dbcb0a41b9dacdd5f8c28ba
- The size of the input paragraph can not be more than 500 words. 
- The structure of the application code base is flat.
- The application is stateless (does not store any information).
- The application has not supported authorization and authentication.
- The application has not supported logging.
- Swagger API documentation was not generated.
- The REST API is supported only by a POST method for each endpoint.
- The application is deployed with Gunicorn and nginx as a reverse proxy.

## Project description
All API requests should have the versioning prefix '/api/v1.0'.

Unit tests are implemented in tests.py. Test data is located in test_data.py.

The REST API provides the following endpoints:
1. POST /api/v1.0/word_frequency_counter - This endpoint accepts a JSON payload containing a string field with the input paragraph to analyze. It returns a JSON object with the counts of each word.
2. POST /api/v1.0/word_counter - This endpoint accepts a JSON payload containing a string field with the input paragraph to analyze. It returns the total count of words.
3. POST /api/v1.0/char_counter - This endpoint accepts a JSON payload containing a string field with the input paragraph to analyze. It returns a JSON object with the total count of characters with spaces and without spaces.

An example of a request:
```
$ 
curl -X POST http://localhost:8080/api/v1.0/word_frequency_counter -H "Content-Type: application/json" -d '{"string": "Hello world!"}'
```

## Deploy with docker compose
```
$ docker compose up -d
```
