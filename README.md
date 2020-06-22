# Super Dungeon Explore Cards API

This API has a list of heroes and monsters from the Super Dungeon Universe.

# API Documentation

## The root path for this version of your API

```
https://sde-api.herokuapp.com
```
## Authentification.

1. No authentification is required.

## Endpoints

* /explorecard  --  Get a list of all available cards.
* /explorecard/<id>  --  Get a specific card by ID.
* /explorecard/name/  --  Get a list of all available cards.
* /explorecard/name/<name>  --  Get a specific card by name.
* /explorecard/type/  --  Get a list of all available cards.
* /explorecard/type/<type>  --  Get a specific card by type.


# HTTP Methods

* GET /explorecard/  -  Returns a list of all categories and subcategories.
```
    https://sde-api.herokuapp.com/explorecard/
```

* GET /explorecard/cardID  -  Returns the explorecard with _id = cardID.
```
    https://sde-api.herokuapp.com/explorecard/5
```

* GET /explorecard/name/  -  Returns a list of all categories and subcategories.
```
    https://sde-api.herokuapp.com/explorecard/name/
```

* GET /explorecard/name/<cardname>  -  Returns the explorecard with name = cardname.
```
    https://sde-api.herokuapp.com/explorecard/name/Moon Princess
```

* GET /explorecard/type/  -  Returns a list of all categories and subcategories.
```
    https://sde-api.herokuapp.com/explorecard/type/
```

* GET /explorecard/type/<cardtype>  -  Returns the explorecard with type = cardtype.
```
    https://sde-api.herokuapp.com/explorecard/type/Monster
```
