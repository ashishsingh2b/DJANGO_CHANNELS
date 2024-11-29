from django.shortcuts import render, redirect

def chatPage(request, room_name=None, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    
    # Use a default room name if none is provided
    if room_name is None:
        room_name = 'default_room'

    context = {
        'room_name': room_name
    }
    return render(request, "chat/chatPage.html", context)
