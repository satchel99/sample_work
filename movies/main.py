import numpy as np
import csv, string
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, neighbors
from scipy import spatial

def get_users():
    f = open("ratings.csv")
    dic = {}
    for i in f.readlines():
        l = i.strip().split(",")
        name = l[0]
        if name in dic:
            dic[name].append((l[1],l[2]))
        else:
            dic[name] = [(l[1],l[2])]
    return dic

def find_movie(movie_id, movies):
    for i in range(0, len(movies)):
        if(movies[i]["id"] == movie_id):
            return i
    return -1

def get_ratings_dic():
    ratings = {}
    f = open("ratings.csv")
    for i in f.readlines():
        l = i.split(",")
        if(l[1] in ratings):
            ratings[l[1]].append((l[0], l[2]))
        else:
            ratings[l[1]] = [(l[0], l[2])]
    return ratings

def construct_profile():
    ratings = get_ratings_dic()
    movies = []
    f = open("movies.csv")
    for i in f.readlines():
        dic = {}
        l = i.split(",")
        dic["id"] = l[0]
        dic["title"] = l[1]
        dic["genres"] = l[2].strip().split("|")
        if(dic["id"] in ratings):
            dic["ratings"] = ratings[dic["id"]]
        movies.append(dic)
    return movies

def display_movies():
    movies = construct_profile()
    for i in movies:
        print(i["id"], i["title"])
        
def lookup_movie(movie_id, movies):
    index = find_movie(movie_id, movies)
    if(index == -1):
        print("movie not found")
    else:
        movie = movies[index]
        print("Movie title", movie["title"])
        print("Genres", movie["genres"])
        if("ratings" in movie):
            print("Ratings", movie["ratings"])
            
def centerd_cosine(movie_1, movie_2, movies):
    index_1 = find_movie(movie_1, movies)
    index_2 = find_movie(movie_2, movies)
    if(index_1 == -1):
        print(movie_1, "not found")
    elif(index_2 == -1):
        print(movie_1, "not found")
    else:
        movie1 = movies[index_1]
        movie2 = movies[index_2]
        if(("genres" in movie1) and ("genres" in movie2)):
            words = []
            for i in movie1["genres"]:
                if i in words:
                    pass
                else:
                    words.append(i)
            for i in movie2["genres"]:
                if i in words:
                    pass
                else:
                    words.append(i)
            l1 = []
            l2 = []
            for i in words:
                l1.append(movie1["genres"].count(i))
                l2.append(movie2["genres"].count(i))
            #print(words, l1, l2)
            return 1 - spatial.distance.cosine(l1, l2)
        else:
            print("cant compute")
    return -1

def knn_set(movie_id, n, movies):
    names = []
    for movie in movies:
        if movie["id"] != movie_id:
            a = centerd_cosine(movie_id, movie["id"], movies)
            if(a != -1):
                temp = []
                temp.append(movie["id"])
                temp.append(a)
                names.append(temp)
    def func(e):
        return e[1]
    names.sort(key=func)
    names.reverse()
    return names[:n]

def display_set(l, movies):
    for i in l:
        id_n = i[0]
        loc = find_movie(id_n, movies)
        movie = movies[loc]
        print("title:", movie["title"])
        print("genres:", movie["genres"])
        print("--------------")
        
def knn(movies, movie_id, users, user_id):
    name = []
    classifier = []
    ratings = []
    ranked_movies = users[user_id]
    for movie in ranked_movies:
        name.append(int(movie[0]))
        ratings.append(float(movie[1]))
        a = centerd_cosine(movie_id, movie[0], movies)
        classifier.append(a)
    features = zip(classifier, classifier)
    X = np.asarray(classifier)
    X = X.reshape(-1,1)
    #print(X)
    y = np.asarray(ratings)
    #print(y)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test, y_test)
    #print(accuracy)
    example_vals = np.asarray([1])
    example_vals = example_vals.reshape(1,-1)
    #print(example_vals)
    prediction = clf.predict(example_vals)
    #print(prediction)
    nabes = clf.kneighbors(example_vals, 5)
    neighborIndecies = nabes[1].tolist()[0]
    neighborsListReturn = []
    for i in neighborIndecies:
        neighborsListReturn.append(name[i])
    return (prediction, neighborsListReturn)

def main():
    menu_str = "What would you like to do?\n1. Display all movies.\n2.lookup a movie\n3.Compute Centered Cosine\n4.See the nearest neighbors set\n5.Find suggested movies\n6.Quit\n"
    movies = construct_profile()
    users = get_users()
    #try:
    keep_going = True
    while(keep_going):
        option = int(input(menu_str))
        if(option == 1):
            display_movies()
        elif(option == 2):
            id_num = int(input("Please enter the id of the movie you want to find: "))
            lookup_movie(str(id_num), movies)
        elif(option == 3):
            id_1 = int(input("Please enter the id of the first movie: "))
            id_2 = int(input("Please enter the id of the second movie: "))
            print("centered_cosine", centerd_cosine(str(id_1), str(id_2), movies))
        elif(option == 4):
            id_1 = int(input("Please enter the id of the first movie: "))
            l = knn_set(str(id_1), 5, movies)
            display_set(l, movies)
        elif(option == 5):
            person = int(input("Please enter the id of the user: "))
            id_1 = int(input("Please enter the id of a movie: "))
            tup = knn(movies, str(id_1), users, str(person))
            print("this is how the user might have ranked this movie")
            print(tup[0])
            print("\n")
            l = tup[1]
            print(l)
            print("based on how the user rated movies these are 5 other movies they might like:")
            for i in range(0, len(l)):
                l[i] = str(l[i])
            display_set(l, movies)
            
        elif(option == 6):
            print("goodbye!")
            keep_going = False
            break
    #except:
        #print("Please enter an integer between 1 an 2")

if __name__ == '__main__':
    main()