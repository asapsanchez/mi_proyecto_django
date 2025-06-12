from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def new_listing(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.seller = request.user
            car.save()
            return redirect('listing_detail', listing_id=car.id)
    else:
        form = CarForm()

    return render(request, 'listings/new_listing.html', {'form': form})



# --- LISTA PRINCIPAL ---
def home(request):
    cars = Car.objects.all()           # por ahora podrías dejarla vacía
    return render(request, 'listings/home.html', {'cars': cars})
    # si aún no tienes plantilla, pon temporalmente:
    # return HttpResponse("Página de inicio (lista de autos)")

# --- DETALLE ---
def listing_detail(request, listing_id):
    car = get_object_or_404(Car, pk=listing_id)
    return render(request, 'listings/detail.html', {'car': car})

