# docker-mysql
This is an application to show the ability to use a docker container of a MySQL database.  
The application uses the Flask SQL Alchemy ORM in combination with PyMySQL to connect to the MySQL database in another container.
<br />
## Starting the container
Start the containers using: `> docker-compose up`  
<br />
## Adding data into the database
Using curl to add data into the database. Note that the */add* route only accepts POST requests  
**Form Data:** `> curl -X POST -d 'greeting=Hello' http://localhost:5000/add`  
**JSON Data:** `> curl -X POST -d '{"greeting":"Hello"}' http://localhost:5000/add`  
**Query String Data:** `> curl -X POST http://localhost:5000/add?greeting=Hello`  
<br />
## Show JSON response for items in the database
Using curl we can request the data as a JSON response from the application. Note that the **/api** route only accepts GET requests
The get all items from the database: `> curl http://localhost:5000/api`  
<br />
## Testing HTTP request methods and data payload
Before inserting data into the database, the **/methods** route can show if the request is a GET, POST, PUT or DELETE method.  
This route can also confirm if the curl request has a data payload with it as well.  
<br />
## Stopping the container
Stop the containers using: `> docker-compose down`

