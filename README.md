# Python Flask Graphene SqlAlchamey

## Setup
install the pipenv package
`pip install pipenv`

Add a `.env` file from the `.env-sample`

## Install packages
`pipenv install`

## Startup app
`flask run`
App is now running at http://127.0.0.1:5000/

## Graphql
http://127.0.0.1:5000/graphql

```
{
  allApplications {
    edges {
      node {
        id,
        state
      }
    }
  }
}
```