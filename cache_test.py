# coding=utf-8
# SI 507 F17 Project 2 - Objects
import requests
import json
import unittest

# Instructions for each piece to be completed for this project
# can be found in the file, below.

# To see whether your problem solutions are passing the tests,
# you should run the Python file: si507f17_project2_objects_tests.py,
# which should be saved in the same directory as this file.

# (DO NOT change the name of this file! Make sure to re-save it
# with the name si507f17_project2_objects_code.py if you change the name.
# Otherwise, we will not be able to grade it!)

# Useful additional references for this part of the homework
# from outside class material:
# - the iTunes Search API documentation:
# - the following chapters from the textbook (also referred to in SI 506):
#   *Classes/ThinkingAboutClasses
#   *Classes/ClassesHoldingData
#   *UsingRESTAPIs/cachingResponses
# - and possibly other chapters, as a reference!

# The first problem to complete for this project can be found below.

# You can search for a variety of different types of media with
# the iTunes Search API: songs, movies, ebooks and audiobooks... (and more)
# You'll definitely need to check out the documentation to understand/recall
# how the parameters of this API work:
# https://affiliate.itunes.apple.com/resources/documentation/
# itunes-store-web-service-search-api/

# Here, we've provided functions to get and cache data from the iTunes Search
# API, but looking at the information in that documentation will help you
# understand what is happening when the second function below gets invoked.
# Make sure you understand what the function does, how it works, and how
# you could invoke it to get data from iTunes Search about e.g. just songs
# corresponding to a certain search term, just movies, or just books.
# Refer to the textbook sections about caching, linked above,
# to help understand these functions!

# You may want to try them out and see what data gets returned,
# in order to complete the problems in this project.


def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


def sample_get_cache_itunes_data(search_term, media_term="all"):
    CACHE_FNAME = 'cache_test.json'
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {}
    baseurl = "https://itunes.apple.com/search"
    params = {}
    params["media"] = media_term
    params["term"] = search_term
    unique_ident = params_unique_combination(baseurl, params)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        reqget = requests.get(baseurl, params=params).text
        CACHE_DICTION[unique_ident] = json.loads(reqget)
        full_text = json.dumps(CACHE_DICTION)
        cache_file_ref = open(CACHE_FNAME, "w")
        cache_file_ref.write(full_text)
        cache_file_ref.close()
        return CACHE_DICTION[unique_ident]

sia = sample_get_cache_itunes_data("sia")

# The Media class constructor should accept one dictionary data structure
# representing a piece of media from iTunes as input to the constructor.

# Saul: This "one dictionary data structure" input should be (e.g.)
# sia["results"][0] (and indeed, is something like this in the tests file).

# It should instatiate at least the following instance variables:
# 1. title
title = sia["results"][0]["trackName"]
print("TITLE: " + str(title))
# 2. author
author = sia["results"][0]["artistName"]
print("AUTHOR: " + str(author))
# 3. itunes_URL
itunes_URL = sia["results"][0]["trackViewUrl"]
print("ITUNES_URL: " + str(itunes_URL))
# 4. itunes_id (e.g. the value of the track ID, whatever the track is in
#   the data... a movie, a song, etc)
itunes_id = sia["results"][0]["trackId"]
print("ITUNES_ID: " + str(itunes_id))
