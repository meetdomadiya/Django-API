# Django-API

This API provides a simple interface for managing a collection of drinks. It allows clients to perform CRUD (Create, Read, Update, Delete) operations on drink resources. The API supports both listing all available drinks and interacting with individual drink records.

## Endpoints

### 1. GET /drinks/
Retrieve a list of all drinks.

* **Response:** Returns a JSON array of drink objects.

* **Status Codes:**
  * **200 OK:** Successfully retrieved the list of drinks.
 
### 2. POST /drinks/
Create a new drink.

* **Request Body:** A JSON object containing **name** and **description** fields.
* **Response:** Returns the created drink object.
* **Status Codes:**
    * **201 Created:** Successfully created a new drink.
    * **400 Bad Request:** Invalid data provided.

### 3. GET /drinks/{id}/
Retrieve details of a specific drink by its ID.

* **Response:** Returns a JSON object of the drink.
* **Status Codes:**
    * **200 OK:** Successfully retrieved the drink.
    * **404 Not Found:** Drink with the specified ID does not exist.
### 4. PUT /drinks/{id}/
Update an existing drink by its ID.

* **Request Body:** A JSON object containing updated **name** and/or **description** fields.
* **Response:** Returns the updated drink object.
* **Status Codes:**
    * **200 OK:** Successfully updated the drink.
    * **400 Bad Request:** Invalid data provided.
    * **404 Not Found:** Drink with the specified ID does not exist.

### 5. DELETE /drinks/{id}/
Delete an existing drink by its ID.

* **Response:** No content.
* **Status Codes:**
    * **204 No Content:** Successfully deleted the drink.
    * **404 Not Found:** Drink with the specified ID does not exist.
