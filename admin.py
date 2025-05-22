# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("credentials.json")
# firebase_admin.initialize_app(cred)



import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firebase_access():
    # Initialize the Firebase Admin SDK.
    try:
        cred = credentials.Certificate("credentials.json")
        # default_app = firebase_admin.initialize_app(cred)
        default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        # return True
        return db
    except Exception as e:
        # print(f"Error initializing Firebase: {e}")
        # return False
        return None

def upload_resorts(db, json_file):
    # upload movies to the firebase
    try:
        # open the json
        with open (json_file, "r") as f:
            resorts = json.load(f)

            # create a db collection in firebase
            resorts_ref = db.collection("movies")

            # write each movie to firebase
            for resort in resorts:
                doc_id = str(resort["id"])
                resorts.document(doc_id).set(resort)

            print(f"Sucessfully uploaded {len(resorts)} resorts.")
    except Exception as e:
        print(f"Error uploading movies: {e}")

# def do_title_query(db, param):
#     # Executes a title query on database
    
#     # get collection and set up query
#     movie_ref = db.collection("movies")
#     query_ref = movie_ref.where(filter=firestore.FieldFilter(param[0], "==", param[1]))
#     results = []

#     # return list
#     return_list = []
#     # store results in results
#     for doc in query_ref.stream():
#         results.append(doc.to_dict())
    
#     # should only be one otherwise issue
#     if len(results) > 1:
#         return_list.append("error in query")
#     elif len(results) == 0:
#         return_list.append("no information")
#     else:
#         # collect movie info
#         movie = results[0]
#         return_list.append(movie["title"])
#         return_list.append(movie["runtime"])
#         return_list.append(movie["genre"])
#         return_list.append(movie["gross"])
#     return return_list

# def do_genre_query(db, param):
#     # Executes a genre query on Firebase

#     # collection and query information prepared
#     movie_ref = db.collection("movies")
#     query_ref = movie_ref.where(filter=firestore.FieldFilter("genre", "==", param[1]))
#     # lists to collect results, and set up return list if no information from query
#     results = []
#     return_list = []

#     # collect query results
#     for doc in query_ref.stream():
#         results.append(doc.to_dict())
    
#     # check amount of results
#     if len(results) == 0:
#         return_list.append("no information")
#     else:
#         # collect title info for movies
#         for movie in results:
#             movie_title = movie['title']
#             return_list.append(movie_title)
#     return return_list

# def do_runtime_query(db, param):
#     # Executes a runtime query
#     movie_ref = db.collection("movies")
#     if len(param) != 3:
#         return['invalid query']
#     try:
#         query_ref = movie_ref.where(filter=firestore.FieldFilter("runtime", param[1], int(param[2])))
#     except ValueError:
#         return['invalid query']

#     # lists to collect results, and set up return list if no information from query
#     results = []
#     return_list = []
    
#     # collect query results
#     for doc in query_ref.stream():
#         results.append(doc.to_dict())

#     # check amount of results
#     if len(results) == 0:
#         return_list.append("no information")
#     else:
#         # collect title info for movies
#         for movie in results:
#             movie_title = movie['title']
#             return_list.append(movie_title)
#     return return_list
    
# def do_gross_query(db, param):
#     # Executes a gross query on Firebase
#     # query and collection information
#     movie_ref = db.collection("movies")
#     if len(param) != 3:
#         return['invalid query']
#     try:
#         query_ref = movie_ref.where(filter=firestore.FieldFilter("gross", param[1], int(param[2])))
#     except ValueError:
#         return['invalid query']
#     # lists to collect results, and set up return list if no information from query
#     results = []
#     return_list = []

#     # collect query results
#     for doc in query_ref.stream():
#         results.append(doc.to_dict())
    
#     # should only be one otherwise issue
#     if len(results) == 0:
#         return_list.append("no information")
#     else:
#         # collect movie info
#         for movie in results:
#             movie_title = movie['title']
#             return_list.append(movie_title)
#     return return_list

# def do_and_query(db, params):
#     # Executes the and query
#     movie_ref = db.collection("movies")

#     # Ensure parameters form valid conditions
#     if len(params) not in [5, 6]:
#         return ["invalid query"]

#     # Process query parameters
#     processed_params = []
#     i = 0
#     while i < len(params):
#         field = params[i]

#         # Handle genre/title (only two elements)
#         if field in ["genre", "title"]:
#             if i + 1 >= len(params):
#                 return ["invalid query"]
#             processed_params.append([field, "==", params[i + 1]])
#             i += 2  # Move past this condition

#         # Handle numerical conditions (three elements)
#         elif field in ["runtime", "gross"]:
#             if i + 2 >= len(params):
#                 return ["invalid query"]
#             try:
#                 processed_params.append([field, params[i + 1], int(params[i + 2])])
#             except ValueError:
#                 return ["invalid query"]
#             i += 3  # Move past this condition

#         else:
#             return ["invalid query"]

#     # Building firestore index query
#     query_ref = movie_ref
#     for query in processed_params:
#         query_ref = query_ref.where(
#             filter=firestore.FieldFilter(query[0], query[1], query[2])
#         )

#     # get results
#     return_list = []
#     for doc in query_ref.stream():
#         return_list.append(doc.to_dict()["title"])  # Collect all matching titles

#     return return_list if return_list else ["no information"]