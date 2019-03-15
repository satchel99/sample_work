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

dic = get_users()
max_ratings = 0
for i in get_users():
    if len(dic[i]) > max_ratings:
        max_ratings = len(dic[i])
        
        
        
        
        
def knn(movies, movie_id, users, user_id):
    name = []
    classifier = []
    ratings = []
    ranked_movies = users[user_id]
    for movie in movies:
        name.append(int(movie[0]))
        ratings.append(int(movie[1]))
        a = centerd_cosine(movie_id, movie[0], movies)
        classifier.append(a)
    features = zip(name, classfier)
    X = np.asarray(features)
    y = np.asarray(ratings)
    print(X)
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    example_vals = np.asarray([int(movie_id),1])
    
    prediction = clf.predict(example_vals)
    print(prediction)
    
    nabes = clf.kneighbors(example_vals, n)
    neighborIndecies = nabes[1].tolist()[0]
    print ("\n\n\n")
    print ("Inputted Values are: ")
    print example_vals
    print ("5 closest neighbors are: ")
    neighborsListReturn = []
    for i in neighborIndecies:
        neighborsListReturn.append(l[i])
    return neighborsListReturn


    