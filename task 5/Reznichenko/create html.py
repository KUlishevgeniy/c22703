import psycopg2


f = open('mysite/templates/index.html', 'w', encoding='utf-8')

html_template = """{% load static %}
<html>
<!DOCTYPE html>
<html style="font-size: 16px;" lang="ru"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="Sample Title, 01">
    <meta name="description" content="">
    <title>The best pictures</title>
    <link rel="stylesheet" href="{% static 'nicepage.css' %}" media="screen">
<link rel="stylesheet" href="{% static 'Страница-2.css' %}" media="screen">
    <script class="u-script" type="text/javascript" src="jquery-1.9.1.min.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
    <meta name="generator" content="Nicepage 5.10.4, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    <link id="u-page-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald:200,300,400,500,600,700">

  
  <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": ""
}</script>
    <meta name="theme-color" content="#b1363e">
    <meta property="og:title" content="Страница 2">
    <meta property="og:type" content="website">
  <meta data-intl-tel-input-cdn-path="intlTelInput/"></head>
  <body data-home-page="https://website4955477.nicepage.io/Страница-2.html?version=e0293f40-c809-4233-883f-e1943bb581cf" data-home-page-title="Страница 2" class="u-body u-xl-mode" data-lang="ru"> 
    <section class="u-clearfix u-image u-shading u-section-1" id="sec-a64f" data-image-width="1080" data-image-height="720">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-container-style u-expanded-width-sm u-expanded-width-xs u-group u-group-1">
          <div class="u-container-layout u-valign-middle-sm u-valign-middle-xs">
            <h1 class="u-custom-font u-font-oswald u-text u-title u-text-1">Лушчие работы художников мира</h1>
            <h4 class="u-text u-text-2">Картины, которые должен знать каждый</h4>
          </div>
        </div>
      </div>
    </section>"""

conn = psycopg2.connect(dbname='db', user='postgres', password='Q1w2e3r4', host='localhost')
cursor = conn.cursor()

for i in range(1, 20):
    cursor.execute(f"SELECT * FROM public.pictures WHERE id = {i}")
    record = cursor.fetchall()
    path = "{% static '" + str(record[0][-1]) + "' %}"
    html_template += f"""<html>
        <section class="u-clearfix u-image u-section-2" id="sec-5d8f" data-image-width="3201" data-image-height="2801">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-clearfix u-expanded-width u-layout-wrap u-layout-wrap-1">
          <div class="u-layout">
            <div class="u-layout-col">
              <div class="u-size-35">
                <div class="u-layout-row">
                  <div class="u-container-style u-layout-cell u-left-cell u-size-30 u-layout-cell-1">
                    <div class="u-container-layout u-container-layout-1">
                      <div class="u-container-style u-expanded u-group u-palette-3-dark-2 u-shape-rectangle u-group-1">
                        <div class="u-container-layout u-container-layout-2">
                          <h1 class="u-custom-font u-font-oswald u-text u-title u-text-1">
                            <br>{record[0][1]}<br>
                            <span style="font-size: 2.25rem;">{record[0][2]}<br>{record[0][3]}
                            </span>
                            <br>
                            <br>
                          </h1>
                          <div class="u-border-3 u-border-white u-line u-line-horizontal u-line-1"></div>
                        </div>
                      </div>
                      <h1 class="u-custom-font u-font-oswald u-text u-text-palette-5-base u-title u-text-2">{i}</h1>
                    </div>
                  </div>
                  <div class="u-container-style u-layout-cell u-right-cell u-size-30 u-layout-cell-2">
                    <div class="u-container-layout">
                      <img class="u-image u-image-1" src="{path}" alt="Картинка">
                    </div>
                  </div>
                </div>
              </div>
              <div class="u-size-30">
                <div class="u-layout-row">
                  <div class="u-align-left u-container-style u-layout-cell u-left-cell u-right-cell u-size-60 u-layout-cell-3">
                    <div class="u-container-layout u-container-layout-4">
                      <p class="u-text u-text-default u-text-3">{record[0][4]}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    print(record[0][-1])

conn.close()
f.write(html_template)
f.close()

