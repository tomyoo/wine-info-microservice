# Vintage Information

This endpoint retrieves detailed data about vintage(s) and the corresponding characteristics.

## Get Vintage information
### `GET /vintages/<id>`

Retrieves all information about a vintage.


#### Response

Field Name         | Field Type | Description
:----------------- | :--------- | :----------
vintage_id         | Integer    | Internal identifyer ID number for specific vintages.
year               | Integer    | The vintage year of the wine, or Null if there is no vintage.
short_tasting_note | String     | A short description of the wine from our tasters.
tasting_note       | String     | The full description of the wine from our tasters.
attributes         | Object     | Each on a 0-5 scale. There will be four attributes, depending on the color of the wine. See table below for more details on the attributes.
region             | Array      | An array containing the regions of the vintage.
grapes             | Array      | A list of the type(s) of grapes that are in the wine.
tastes             | Array      | A list of flavor(s) that the vintage invokes.
pairings           | Array      | A list of food(s) to pair the vintage with.
traits             | Array      | A list of trait(s) of the vintage.
wine               | Object     | The information about the vintage's corresponding wine. See table below for details.
image_urls         | Object     | The URLs for the image resources for the wine on a CDN. See table below for details.

##### Wine

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

##### Attributes

Each on a scale of 0 (least) to 5 (most).

Attribute Name  | Field Type | Description
:-------------- | :--------- | :----------
body            | Integer    | How full bodied the wine is.
fruit           | Integer    | How fruity the wine is.
earth           | Integer    | Only for `"red"`wines. How earthy the wine is.
tannin          | Integer    | Only for `"red"` wines. How tannic the wine is.
oak             | Integer    | Only for `"white"` wines. How oaky, or "buttery", the wine is.
acidity         | Integer    | Only for `"white"` wines. How acidic or sour the wine is.

##### Image URLs

The URLs to display image resources related to the bottle. If no image exists for the label or bottle, the corresponding field will have the value `null`.

Attribute Name  | Field Type | Description
:-------------- | :--------- | :----------
label           | String     | The image of the label
bottle          | String     | The image of the full bottle

#### Sample Vintage Information

```
"data": {
     "type": "vintages",
     "id": "1",
     "attributes": {
         "year": 2015,
         "short_tasting_note": "Aromas of strawberry, raspberry, cherry and flowers waft from the glass, followed by more of the same flavors on the palate.",
         "tasting_note": "This lovely, floral rosé delights with strawberry, raspberry, cherry flavors, a soft and balanced acidity, and more bright, red fruits on the finish. The grapes were gently pressed as whole clusters before aging in stainless steel to maintain the beautiful fruit and floral aromatics.",
         "attributes": {
             "body": 3,
             "fruit": 3,
             "earth": null,
             "tannin": null,
             "oak": 1,
             "acidity": 3
         },
         "region": ["Monterey", "Central Coast", "California", "United States"],
         "grapes": ["Pinot Noir"],
         "tastes": ["cherry", "flowers", "raspberry jam", "tropical fruit"],
         "pairings": ["Asian cuisines", "light salads", "brunch and desserts"],
         "traits": ["Bold"],
     }
     "relationships": {
         "wine": {
             "name": "2015 The Brink Monterey County Pinot Noir Rosé",
             "brand": "The Brink",
             "variety": {
                 "name": "Pinot Noir Rosé",
                 "type": "rosé"
             }
             "classification": {
                 "name": "Pinot Noir Rosé",
                 "type": "rosé"
             }
             "data": {"type": "wines", "id": "9"}
         }
         "image_urls": {
             "label": "https://s3.amazonaws.com/lot18-partner/HelloFresh+Images/01IE000000LZyt_label.jpeg",
             "bottle": "https://s3.amazonaws.com/lot18-partner/HelloFresh+Images/01IE000000LZyt_bottle.png",
             "bottle_thumb": "https://s3.amazonaws.com/lot18-partner/HelloFresh+Images/01IE000000LZyt_bottle_thumb.png"
             "data": [
                 {"type": "urls", "id": "5"},
                 {"type": "urls", "id": "6"},
                 {"type": "urls", "id": "7"}
             ]
         }
    }
}
```

## Get info about multiple vintages
### `GET /vintages`

You can pass a list of `vintage_id`s to this endpoint to get a list
of information about vintages. The information is the same as in the response above.

For example, `GET /vintages?vintage_id=1,2`

#### Request

Field Name      | Field Type          | Description
:-------------- | :------------------ | :----------
vintage_ids     | List of Strings     | The ID of the item.


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
