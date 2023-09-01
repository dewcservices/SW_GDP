# CRUD RestAPI Extension Software Engineering Challenge

## Introduction

In this software engineering challenge, you are tasked to advance your 01/23 challenge code by adding dependency injection (so we can explore mocked implementations and set the codebase up for a future testing challenge) and add a shared devcontainer so all developers are working from developer environment as code.

## Requirements

1. Using springboot complete or refactor your code from python to achieve the required functionality of challenge 01/23.

- Choose a single database table to work with. The table should have at least the following fields:
   - `id` (unique identifier for each record)
   - `name` (string, representing the name of an item)
   - `description` (string, providing additional information about the item)
   - You can add more fields if you wish, but the above three are mandatory.

- Implement the following endpoints:

   - **Create** (HTTP POST):
     - Endpoint: `/items`
     - Description: Allows the user to create a new item by providing the `name` and `description` in the request body.
     - Response: Returns the created item with its unique `id`.

   - **Read** (HTTP GET):
     - Endpoint: `/items/:id`
     - Description: Retrieves the details of a specific item by providing its unique `id`.
     - Response: Returns the item's details (including `name`, `description`, and `id`) if it exists, or an appropriate error message if not found.

   - **Update** (HTTP PUT or PATCH):
     - Endpoint: `/items/:id`
     - Description: Allows the user to update an existing item's `name` and/or `description` by providing the updated values in the request body. The `id` should remain unchanged.
     - Response: Returns the updated item.

   - **Delete** (HTTP DELETE):
     - Endpoint: `/items/:id`
     - Description: Deletes an item with the provided `id`.
     - Response: Returns a success message or an appropriate error message if the item doesn't exist.

- Use swagger to explain and demo how to use your RestAPI, including the endpoints, expected request and response formats, and any additional details.

2. As a team agree on a devcontainers and add to a repo everyone has access to. Everyone is to git submodule the devcontainer into their challenge repo

3. Refactor the code to implement an interface for the service and dao layer

4. Implement a mocked service and dao using interface dependency injection with the Qualifier Springboot attribute

5. Test the mocked service implementation returns the mocked response

6. Implement the real Service using the interface to using the dao mocked implementation
- using Qualifier and Primary springboot annotations move the primary annotation between the Service Mock and real implementations between builds to prove you can change the injected implementaion under the control of where the primary annotation is (note, there should only be one primary annotation)

6. Implement the real dao and test switching the primary annotation between the dao mock and real implementation

## Submission

Once you complete the challenge, create a public GitHub repository and upload your code, along with the documentation, to the repository. Share the repository link with the team.

## Evaluation

Your submission will be evaluated based on the following criteria:

- Usage of devcontainer by git submodule
- Usage and deomonstrated control of Interface DI in springboot
