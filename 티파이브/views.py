from django.shortcuts import render

# Create your views here.

group = {
    'members' : [
        {
            'group_name' : 'T5',
            'name' : '지훈',
            'img_src' : 'https://i.pinimg.com/236x/03/86/e6/0386e661464b0a9968afd93f7a0117ed.jpg',
        },
        {
            'group_name': 'T5',
            'name': '준규',
            'img_src': 'https://i.pinimg.com/236x/af/d0/c8/afd0c827aeecb0e731c13dff87313ba5.jpg',
        }
    ]
}
def show_jihoon(request):
    context = list(filter(lambda member :'지훈' in  member['name'], group['members']))[0]
    # context = group['members'][0]
    return render(request, '티파이브/jihoon.html')
    # return render(request, '티파이브/jihoon.html')

def show_junkyu(request):
    context = list(filter(lambda member :'준규' in  member['name'], group['members']))[1]
    # context = group['members'][1]
    return render(request, '티파이브/junkyu.html')
    # return render(request, '티파이브/junkyu.html')