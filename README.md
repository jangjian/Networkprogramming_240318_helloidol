# helloidol

 - - -

1. startproject helloidol
   1. phthon -m pip install django~=4.2 (4.2의 최신버전 설치)
   2. django-admin startproject _helloidol_ .(현재 디렉토리)
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. _helloidol_/setting.py
      1. 'playground', in INSTALLED_APPS