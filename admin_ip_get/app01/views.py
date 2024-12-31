from django.shortcuts import render

from ipware import get_client_ip
# Create your views here.
def index(request):

    client_ip , is_routable = get_client_ip(request)
    print(client_ip,is_routable)
    if client_ip is None:
        print(client_ip)
    # Unable to get the client's IP address

    else:
        if is_routable:
            print(is_routable)
        # The client's IP address is publicly routable on the Internet
        else:
            # The client's IP address is private
            pass
    return render(request , 'index.html')
