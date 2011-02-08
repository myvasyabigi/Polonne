from django.shortcuts import render_to_response


from models import Album
from models import Photo

def album_list(request):
    """ Return a list of all paginated albums """
    
    albums = Album.objects.all()
    albums = list(albums)
    k = []
    b = []
    counter = 0

    for i in xrange(len(albums)):
	    if counter < 4: 
		    b.append(albums[i])
		    counter += 1
	    if i+1 == len(albums) or len(b) == 4: 
		    k.append(b)
  

        		
    data = {
    "albums":albums,
    "k":k,
    }
    return render_to_response("gallery/gallary.htm", data)
