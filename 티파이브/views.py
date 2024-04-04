from django.shortcuts import render

group = {
    'members': [
        {
            'group_name': 'T5',
            'name': '지훈',
            'img_src' : '티파이브/images/jihoon.jpg'
            # 'img_src': 'https://i.pinimg.com/236x/03/86/e6/0386e661464b0a9968afd93f7a0117ed.jpg',
        },
        {
            'group_name': 'T5',
            'name': '준규',
            'img_src': '티파이브/images/junkyu.jpg'
            # 'img_src': 'https://i.pinimg.com/236x/af/d0/c8/afd0c827aeecb0e731c13dff87313ba5.jpg',
        },
        {
            'group_name': 'T5',
            'name': '재혁',
            'img_src': '티파이브/images/jaehyuk.jpg'
            # 'img_src': 'https://i.pinimg.com/236x/e6/9a/81/e69a811a4784fcae63e7bfc358ab583b.jpg',
        },
        {
            'group_name': 'T5',
            'name': '도영',
            'img_src': '티파이브/images/doyoung.jpg'
            # 'img_src': 'https://i.pinimg.com/236x/e6/9a/81/e69a811a4784fcae63e7bfc358ab583b.jpg',
        },
        {
            'group_name': 'T5',
            'name': '정환',
            'img_src': '티파이브/images/junghwan.jpg'
            # 'img_src': 'https://i.pinimg.com/236x/e6/9a/81/e69a811a4784fcae63e7bfc358ab583b.jpg',
        }
    ]
}

def show_jihoon(request):
    context = list(filter(lambda member: '지훈' in member['name'], group['members']))[0]
    return render(request, '티파이브/member.html', context)

def show_junkyu(request):
    context = list(filter(lambda member: '준규' in member['name'], group['members']))[0]
    return render(request, '티파이브/member.html', context)

def show_jaehyuk(request):
    context = list(filter(lambda member: '재혁' in member['name'], group['members']))[0]
    return render(request, '티파이브/member.html', context)

def show_member(request, member):
    context = list(filter(lambda mem: member in mem['name'], group['members']))[0]
    return render(request, '티파이브/member.html', context)

def show_memberlists(request):
    context = group     #{'members' : [{멤버1}, {멤버2},]}
    return render(request, '티파이브/memberlists.html', context=context)