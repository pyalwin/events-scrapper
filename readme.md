# Events parser

The api is to fetch and parse the events from url "https://www.lucernefestival.ch/en/program/summer-festival-22"

The techstacks used in here are
* fastapi
* postgresql
* docker
* docker-compose
* ormar ( ORM for fastapi )


## Setup and build the api
```
docker-compose build
```

## Run the api
```
docker-compose up -d
```
The api will now be accessible in http://localhost:8000

The document for the api is accessible under http://localhost:8000/redoc


## To scrape the events and load into the database 

Call the parse site end point http://localhost:8000/fetch-events
 with the following input
```
{
    "url": "https://www.lucernefestival.ch/en/program/summer-festival-22"
}
```
Note: The parser is created based on this specific url. 
Hence, any change in html structure will require different parser


## To view list of events already loaded into the database

call the read endpoint http://localhost:8000/events

