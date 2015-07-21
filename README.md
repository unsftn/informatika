# Sajt Katedre za informatiku

## Instalacija i podešavanje

1. Instaliraj Ruby, Bundler i Jekyll kako piše ovde: https://help.github.com/articles/using-jekyll-with-pages/

2. Kloniraj sebi repozitorijum
  ```
  git clone https://github.com/unsftn/informatika.git
  ```

3. Predji na `gh-pages` granu i sve izmene na sajtu radi na njoj
  ```
  git checkout gh-pages
  ```

## Gde su koji fajlovi

1. Lične stranice članova katedre su u folderu `_faculty`. Ako neko nedostaje, treba dodati fajl za tog člana po uzoru na ostale fajlove.

2. Stranice predmeta su u folderu `_courses`. Ako neki predmet nedostaje, treba dodati fajl za taj predmet po uzoru na ostale fajlove.

3. Fotografije/avatari članova katedre treba da stoje u folderu `img/faculty`.

4. Fajlovi za predmete stoje u folderu `files/courses/<predmet>`.

5. Fajlovi za news & events sekciju stoje u folderu `files/events/<datum>`.

6. Fajlovi za članove katedre stoje u folderu `files/faculty/<ImePrezime>`.

