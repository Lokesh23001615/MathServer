from django.shortcuts import render
def surfacearea(request):
    context={}
    context['surfacearea'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Radius=',r)
        print('Height=',h)
        surfacearea = 2*3.14*int(r)*int(h) + 2*3.14*int(r)*int(r)
        context['surfacearea'] = surfacearea
        context['r'] = r
        context['h'] = h
        print('Area=',surfacearea)
    return render(request,'mathapp/math.html',context)

