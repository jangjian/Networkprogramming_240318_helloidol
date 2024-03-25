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
3. playground/
   - 정보 전달 : urls -> views -> (models ->) templetes
   - 코드 작성 : (models -> )views -> templetes -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
   2. urls 
      1. _/playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/ 
    1. urls, playground/urls
       1. _playground/_ -> _hello/_ -> _say_hello()_
       2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
       3. _playground/_ -> _bye_html/_ -> _say_bye_html()_



