from django.shortcuts import render
from forms import UserProfileForm


# Create your views here.
def ProfileView(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST)

		if form.is_valid():
			form.save()
			return render(request, 'gametime/index.html', {'form': form})

	else:
		form = UserProfileForm()

	return render(request, 'gametime/index.html', {'form': form})
