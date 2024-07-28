from flask import Flask
import random
facts_list=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
            "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
            "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
            "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."]


saka_list=["kedi köpeğe ne demiş. cevap ne",
           "kar üzerinde yürüyen adama ne denir? karabasan",
           "sınıftan niye buhar çıkıyormuş? çünkü öğrenciler dersi kaynatıyormuş"]
app = Flask(__name__)

@app.route("/gercekler")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/merhaba")
def merhaba():
    return f'<p>merhaba gercekler sitesine hoş geldiniz</p><a href="/gercekler">rasgele bir şaka!</a><a href="/saka">Rastgele bir gerçeği görüntüle!</a>'
@app.route("/saka")
def saka():
    return f'<p>{random.choice(saka_list)}</p>'
app.run(debug=True)