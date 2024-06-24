# Installation

● Cloning the repository

```
git clone https://github.com/Temskyi/REST-API-task.git
cd REST-API-task
```

● Install dependencies:
  `pip install -r requirements.txt`

● In settings.py, change `SECRET_KEY`

● Migrate the database:
  `python manage.py migrate`

● Create superuser:
  `python manage.py createsuperuser`

● Run the server:
  `python manage.py runserver`

# Endpoints

## Teams

- Create a team:
  - **HTTP Method:** POST
  - **URL:** `/api/v1/team/`
  - **Description:** Allows you to create a new team. Team data is passed in the request body in JSON format.
  - **Example JSON:** `{"name": "Team1"}`

- Get a list of all teams:
  - **HTTP Method:** GET
  - **URL:** `/api/v1/team/`
  - **Description:** Returns a list of all teams.

- Get a team by identifier:
  - **HTTP Method:** GET
  - **URL:** `/api/v1/team/{team_id}/`
  - **Description:** Returns information about the team with the specified identifier.

- Get a list of all people in a specific team:
  - **HTTP Method:** GET
  - **URL:** `/api/v1/team/{team_id}/persons_in_team/`
  - **Description:** Returns a list of all people in the team with the specified identifier.

- Update a team:
  - **HTTP Method:** PUT/PATCH
  - **URL:** `/api/v1/team/{team_id}/`
  - **Description:** Updates information about the team with the specified identifier. Team data is passed in the request body in JSON format.
  - **Example JSON:** `{"id": 1, "name": "FirstTeam"}`

- Delete a team:
  - **HTTP Method:** DELETE
  - **URL:** `/api/v1/team/{team_id}/`
  - **Description:** Deletes the team with the specified identifier.

### Persons

- Create a new person:
  - **HTTP Method:** POST
  - **URL:** `/api/v1/person/`
  - **Description:** Adds a new person to the team with the specified identifier. Person data is passed in the request body in JSON format.
  - **Example JSON:**
    ```json
    {
      "first_name": "Artem",
      "last_name": "Moskalenko",
      "email": "artem.moskalenko.00@gmail.com",
      "team_id": 1
    }
    ```
    
- Get a list of all people:
  - **HTTP Method:** GET
  - **URL:** `/api/v1/person/`
  - **Description:** Returns a list of all people.

- Get a person by identifier:
  - **HTTP Method:** GET
  - **URL:** `/api/v1/person/{person_id}/`
  - **Description:** Returns information about the person with the specified identifier.

- Update person data:
  - **HTTP Method:** PUT/PATCH
  - **URL:** `/api/v1/person/{person_id}/`
  - **Description:** Updates information about the person with the specified identifier. Person data is passed in the request body in JSON format.
  - **Example JSON:**
    ```json
    {
      "first_name": "Artem",
      "last_name": "Moskalenko",
      "email": "artem.moskalenko.00@gmail.com",
      "team_id": 1
    }
    ```

- Delete a person:
  - **HTTP Method:** DELETE
  - **URL:** `/api/v1/person/{person_id}/`
  - **Description:** Deletes the person with the specified identifier.