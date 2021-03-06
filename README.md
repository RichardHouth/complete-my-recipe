Project for CS 4800 - Software Engineering

# Complete My Recipe

Enter the spare ingredients you have in your pantry and receive a list of recipes that include those ingredients and the additional ingredients you need to complete the recipe.

## Input
- spare ingredients (required) PRIORITY
- ingredient amounts (optional)
- number of ingredients you are willing to buy (optional)
- ethnic origins of recipes you wish to complete (optional)

## Output
- recipes to choose from with their respective remaining ingredients

## To-Do (Chronological)

- [ ] Set up the template of front-end according to [this](notes/Rough%20Layout.png)
- [ ] Adjust back-end API accordingly to template
- [ ] Find a way to populate database with appropriate data
- [ ] Connect front-end to back-end
- [ ] Set up API on [pythonanywhere](https://www.pythonanywhere.com/)
- [ ] Create new to-do list for next feature

----------------------------------------------------------------------------------------------------------------------------------------

## Search and Result Features: 
Many of the following features might be implemented in the later stages of the project. Initially we will be focusing on the minimal requirements to get this app functional. I have seperated the functionality by priority below.

## Search Options - Priority:
- Include seperate sections for the main categories of food groups: Protein, Grain, Fruits, Vegetables, Dairy, Miscellaneous
      > From each of these categories there should be a button for adding an ingredient which will then provide the user with a drop-down         menu of ingredients that pertain to that category. If possible, typing in part of the ingredient name should reduce the drop-down         menu to only the ingredients that contain that partial name. Once found, clicking an "Add" button should solidify the ingredient           selection with the ability to also "Delete" the ingredient.
      
## Search Options - Extra Functionality
- Include amounts for ingredients
- Include the ability to EXCLUDE ingredients from search results
- Cusine Options
- Meat Option (i.e. Beef, Chicken, Pork, Fish, Seafood, Vegetarian, Vegan)

## Result Options - Extra Functionality
- Ability to order search results by the following:
      >Prep-Time (Lowest - Highest)
      >Meat Option
      >Amounts of required ingredients (Lowest - Highest)
      
## App Features - Extra Functionality
- "Favority" section for recipes you have "Favorited"
- Recent Recipes section
- Ability to review, edit, and reuse saved searches
