# Wine Information

This endpoint retrieves detailed data about wine(s) and the corresponding characteristics.

## Get Wine information
### `GET /wines/<id>`

Retrieves all information about a wine.


#### Response

Wine   Field Name  | Field Type | Description
:----------------- | :--------- | :----------
name               | String     | The name of the wine.
brand              | String     | The brand of the wine.
variety            | Object     | The information about the wine's corresponding variety. See table below for details.
classification     | Object     | The information about the wine's corresponding classification. See table below for details.

###### Variety

Wine   Field Name  | Field Type | Description
:----------------- | :--------- | :----------
name               | String     | The name of the variety.
type/color         | String     | `"red"`, `"white"`, `"rosé"`, or `"sparkling"`.

###### Classification

Wine   Field Name  | Field Type | Description
:----------------- | :--------- | :----------
name               | String     | The name of the variety.
type/color         | String     | `"red"`, `"white"`, `"rosé"`, or `"sparkling"`.

#### Sample Wine Information

```
"data": {
     "type": "wines",
     "id": "9",
     "attributes": {
         "name": "2015 The Brink Monterey County Pinot Noir Rosé",
         "brand": "The Brink",
     }
     "relationships": {
         "variety": {
             "name": "Pinot Noir Rosé",
             "type": "rosé"
         }
         "classification": {
             "name": "Pinot Noir Rosé",
             "type": "rosé"
         }
         "data": [
             {"type": "varieties", "id": "9"},
             {"type": "classifications", "id": "9"},
         ]
     }
}
```

## Get info about multiple wines
### `GET /wines`

You can pass a list of `vintage_id`s to this endpoint to get a list
of information about vintages. The information is the same as in the response above.

For example, `GET /wines?wine_id=1,2`

#### Request

Field Name      | Field Type          | Description
:-------------- | :------------------ | :----------
wine_ids        | List of Strings     | The ID of the item.


## Triggering Error Responses

### `other_error`

For triggering other_error, use ``-1`` as value for path_parameter.

#### Sample Request:

    GET vintages/-1


#### Response:

```
400 Bad Request
Content-Type: application/json
```

```
{
  "error": {
    "error_type": "other",
    "error_category": "general",
    "message": "Other error.",
    "details": null
  }
}
```
