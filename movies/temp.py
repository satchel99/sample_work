def knn(vals, n):
    l = sortIt(1000,"rank")
    if (n >= len(l)):
        n = len(l) - 2 #to be safe
    rank = []
    acousticness = []
    danceability = []
    density = []
    duration = []
    energy = []
    ideas = []
    instrumentalness = []
    liveness = []
    loudness = []
    speechiness = []
    tempo = []
    valence = []
    words = []
    classifier = []
    for dic in l:
        rank.append(dic["rank"])
        acousticness.append(dic["acousticness"])
        danceability.append(dic["danceability"])
        density.append(dic["density"])
        duration.append(dic["duration"])
        energy.append(dic["energy"])
        ideas.append(dic["ideas"])
        instrumentalness.append(dic["instrumentalness"])
        liveness.append(dic["liveness"])
        loudness.append(dic["loudness"])
        speechiness.append(dic["speechiness"])
        tempo.append(dic["tempo"])
        valence.append(dic["valence"])
        words.append(dic["words"])
    features = zip(acousticness,danceability,density,duration,energy,ideas,instrumentalness,liveness,loudness,speechiness,tempo,valence,words)
    X = np.asarray(classifier)
    y = np.asarray(rank)
    
    if (acousticness == -1.0):
        acousticness = np.mean(X, 0)
    elif (danceability == -1.0):
        danceability = np.mean(X, 1)
    elif (density == -1.0):
        density = np.mean(X, 2)
    elif (duration == -1.0):
        duration = np.mean(X, 3)
    elif (energy == -1.0):
        energy = np.mean(X, 4)
    elif (ideas == -1.0):
        ideas = np.mean(X, 5)
    elif (instrumentalness == -1.0):
        instrumentalness = np.mean(X, 6)
    elif (liveness == -1.0):
        liveness = np.mean(X, 7)
    elif (loudness == -1.0):
        loudness = np.mean(X, 8)
    elif (speechiness == -1.0):
        speechiness = np.mean(X, 9)
    elif (tempo == -1.0):
        tempo = np.mean(X, 10)
    elif (valence == -1.0):
        valence = np.mean(X, 11)
    elif (words == -1.0):
        words = np.mean(X, 12)
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)
    
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    
    example_vals = np.asarray(vals)
    example_vals = example_vals.reshape(1,-1)
    
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