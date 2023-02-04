#For problem 2, you are going to implement an API that our p2client.ipynb notebook is going to call
#You should NOT change p2client.ipynb, and you should give us a fresh database (one that has the necessary table(s) but no data)
#if you want to play around and test your API (which you should), feel free to make an additional file

# You are tasked with creating a flower data management system (FDMS)
# In particular, this FDMS will manage accepting new flower data, querying for flower data, and generating some statistics based on query parameters
# You should implement the following operations:
#  - GET / that returns some kind of Hello World message: it could be an introduction the dataset, a rough description, etc.
#  - PUT /flowers that takes a Flower and stores it in the database (that you need to create as well)
#  - GET /flowers that takes no parameters and returns all Flowers currently in the database
#  - GET /flowers/{genus} that takes a genus of flower and returns all observations of that genus
#  - GET /flowers/{genus}/{species} that takes a species of flower and returns all observations of that species
#  - GET /flowers/{genus}/{species}/petals/avg that takes a species of flower and returns the average petal count across observations
#  - GET /flowers/{genus}/{species}/petals/min that takes a species of flower and returns the minimum petal count across observations
#  - GET /flowers/{genus}/{species}/petals/max that takes a species of flower and returns the maximum petal count across observations

# A Flower should only be accepted with
# - its binomial nomenclature (Genus species, with Genus being capitalized, a space, and then species) as a string
# - a count of how many petals observed (positive integers and 0)
# - a color as a string