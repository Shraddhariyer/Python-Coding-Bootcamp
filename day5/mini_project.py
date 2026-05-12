#to make a movie watchlist
#add movie to watchlist
def add_movie(watchlist):
    name=input("Enter movie name:")
    genre=input("Enter movie genre:")
    movie={
        "name":name,
        "genre":genre,
        "watch":False
    }
    watchlist.append(movie)
    genres.add(genre)
    print("Movie added successfully!!")

#remove movie from watchlist
def remove_movie(watchlist):
    name=input("Enter a movie to remove from watchlist:")
    for movie in watchlist:
        if movie["name"]==name:
            watchlist.remove(movie)
            print("Movie removed!!")
        else:
            print("Movies does not exist!!")

#to add movies to watched list
def watched_movie(watchlist,watched):
    name=input("Enter he movie you watched:")
    for movie in watchlist:
        if movie["name"]==name:
            movie["watch"]=True
            watched.add(name)
            print("Movie added to watched list!!")
        else:
            print("Movie not found")

#display watchlist
def display_watchlist(watchlist):
    if (len(watchlist)==0):
        print("Watchlist is empty...") 
    else:
        print("YOUR WATCHLIST")
        for movie in watchlist:
            print("Movie:",movie["name"])    
            print("Genre:",movie["genre"]) 
            print("Watch:",movie["watch"]) 



#main function
watchlist=[]
watched=set()
genres=set()

while True:
    print("MOVIE WATCHLIST SYSTEM")
    print("Select a choice[1-5]:")
    print("1. Add movie to watchlist")
    print("2. Remove movie from watchlist")
    print("3. Mark movie as watched")
    print("4. Display watchlist")
    print("5. Exit")

    choice=int(input("Enter you choice[1-5]:"))
    if choice==1:
        add_movie(watchlist)
    elif choice==2:
        remove_movie(watchlist)
    elif choice==3:
        watched_movie(watchlist,watched)
    elif choice==4:
        display_watchlist(watchlist)
    elif choice==5:
        print("Existing..")
        break
    else:
        print("Invalid option")
