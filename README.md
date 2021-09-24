# Simple-API-for-Recipes
Create a simple Back-End API for accessing, adding, and updating recipes in a JSON data file.

Original problem is descibed by Hatchway's sample exercise for building a back-end API. The API is designed to fulfill the following requirements:
  1. Access recipes that currently already exist in the JSON file.
  2. Get all recipe names in the file.
  3. Get recipe ingredients and number of steps for a specific recipe in the file. If recipe not in file, return an error message.
  4. Add a new recipe to file. If recipe already exists, return an error message.
  5. Update an existing recipe in the file. If recipe does not exist, return an error message.

This repository represents my attempt at creating a solution for their exercise. The API is written in Python. 

# HOW TO USE CODE:
1. code requires Flask which can be installed with "pip -install -U Flask"

# FUTURE TO-DOs:
1. Could include a new route to remove recipe from file.
