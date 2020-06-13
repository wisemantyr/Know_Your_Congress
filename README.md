# Know Your Congress

## Know how they vote, when they vote, if they vote

Our team was interested in the congresspeople that represent each of us. We want to make this data exciting and easily accessible through an interactive dashboard.

To accomplish this we used the ProPublic Congress API. We queried the API with Python requests and json libraries then used PyMongo to upload the JSON responses to a Mongo database. We served the Flask API routes from the database collections. 

The dashboard includes member demographics based on a dropdown menu using D3.js, a D3.js scatterchart with aggregated data about all congressmembers, a Plotly bar chart displaying a breakdown of how political parties have voted on recent bills, and a mapbox map of congressional districts.

The following tools were used:

Python:
  - flask
  - PyMongo
  - requests
  - json
  - geopandas

Javascript:
  - dijit
  - D3
  - D3 tip 
  - mapbox gl

HTML/CSS:
  - Bootstrap

MongoDB

## INSTRUCTIONS FOR USE

Python Depedencies:
  - flask
  - pymongo
  - requests
  - json
  - geopandas

Files to include in .gitignore:
  - config.py
  - config.js
  - cd_116.geojson
  - \_\_pycache_\_

Files needed:
  - config.py in the same directoy as app.py with ProPublica Congress API key as a variable named "key" (get here: https://projects.propublica.org/api-docs/congress-api/)
  - config.js in the static/js directory with a MapBox access token as const variable named "MAP_API" (get here: https://www.mapbox.com/)

Steps to run the flask app sucessfully:

1. Run the convertGeoJSON.py script in the geo_data directory to create the GeoJSON file for the map. This file needs to be created by every user as it is too large for GitHub to store. The file is included in the .gitignore.

2. Run the buildDB.py script in the main directory to create the mongo database. Ensure connection to mongo prior to running. This script will not run if step 1 is not completed as it creates a features collection in the database from the GeoJSON file. While this collection is not currently being used, we have used it for reference and may find a use for it in the future.

3. Run the app.py script in the main directory.

#### CREDIT TO:
ProPublica for the API: https://projects.propublica.org/api-docs/congress-api/

unitedstates GitHub for Congressmembers photos: https://github.com/unitedstates/images/tree/gh-pages/congress/225x275

Data.gov for congressional districts shapefile: https://catalog.data.gov/dataset/tiger-line-shapefile-2018-nation-u-s-116th-congressional-district-national
