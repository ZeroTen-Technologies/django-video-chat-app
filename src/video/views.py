from django.shortcuts import render

# Create your views here.

def video_view(request):
	context = {}
	return render(request, 'video/index.html', context=context)
