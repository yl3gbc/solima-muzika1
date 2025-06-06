from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    title = 'pr.Andra Solima mūzikas '
    return render_template('index.html', title=title)

@app.route( '/jaunakie')
def jaunakie():
    title = 'Jaunākie raksti'
    return render_template('jaunakie.html', title=title)

@app.route('/generalpart')
def generalpart():
    title = 'Visi gabali'
    return render_template('generalpart.html', title=title)

@app.route('/Vissvetakasakramentagodam')
def Vissvetakasakramentagodam():
    title = 'Vissvētākā Sakramenta godam'
    return render_template('tematiskaissadalijums/Vissvetakasakramentagodam.html', title=title)

@app.route('/JezusSirdsKungaJezusgodam')
def JezusSirdsKungaJezusgodam():
    title = 'Jēzus Sirds/Kunga Jēzus godam'
    return render_template('tematiskaissadalijums/JezusSirdsKungaJezusgodam.html', title=title)

@app.route('/Dievagodam')
def Dievagodam():
    title = 'Dieva godam'
    return render_template('tematiskaissadalijums/Dievagodamdam.html', title=titl)

@app.route('/SvetaGaragodam')
def SvetaGaragodam():
    title = 'Svētā Gara godam'
    return render_template('tematiskaissadalijums/SvetaGaragodam.html', title=title)

@app.route('/VissvetasTrisvienibasgodam')
def VissvetasTrisvienibasgodam():
    title = 'Vissvētās Trīsvienības godam'
    return render_template('tematiskaissadalijums/VissvetasTrisvienibasgodam.html')

@app.route('/Dievmatesgodam')
def Dievmatesgodam():
    title = 'Dievmātes godam'
    return  render_template('tematiskaissadalijums/Dievmatesgodam.html')

@app.route('/udenssvetibaslaika')
def udenssvetibaslaika():
    title = 'Ūdens svētības laikā:'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/udenssvetibaslaika.html')

@app.route('/Lieldienulaika1')
def Lieldienulaika():
    title = '(Lieldienu laikā)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/Lieldienulaika1.html')

@app.route('/KyrieKungsapzelojiesparmums1')
def KyrieKungsapzelojiesparmums1():
    title = 'Kyrie (Kungs, apžēlojies par mums)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/KyrieKungsapzelojiesparmums1.html')

@app.route('/GloriaGods1')
def GloriaGods1():
    title = 'Gloria (Gods)'
    return  render_template('tematiskaissadalijums/SvetasMisesdalas/GloriaGods1.html')

@app.route('/StarplasijumuPsalmi')
def StarplasijumuPsalmi():
    title = 'Starplasījumu Psalmi'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/StarplasijumuPsalmi.html')

@app.route('/Alleluja')
def Alleluja():
    title = 'Alleluja'
    return  render_template('tematiskaissadalijums/SvetasMisesdalas/Alleluja.html')

@app.route('/Gaveni1')
def Gaveni1():
    title = '(Gavēnī)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/Gaveni1.hml')

@app.route('/CredoEsticu1')
def CredoEsticu1():
    title = 'Credo (Es ticu)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/CredoEsticu1.html')

@app.route('/SuplikacijasSvetaisDievs1')
def SuplikacijasSvetaisDievs1():
    title = 'Suplikācijas (Svētais Dievs)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/SuplikacijasSvetaisDievs1.html')

@app.route('/SanctusSvets1')
def SanctusSvets1():
    title = 'Sanctus (Svēts)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/SanctusSvets1.html')

@app.route('/Aklamacijapeckonsekracijas')
def Aklamacijapeckonsekracijas():
    title = 'Aklamācija pēc konsekrācijas '
    return render_template('tematiskaissadalijums/SvetasMisesdalas/Aklamacijapeckonsekracijas.html ')

@app.route('/DoksologijasAmen')
def DoksologijasAmen():
    title = 'Doksoloģijas "Amen" '
    return render_template('tematiskaissadalijums/SvetasMisesdalas/DoksologijasAmen.html ')

@app.route('/AgnusDeiDievaJers')
def AgnusDeiDievaJers():
    title = 'Agnus Dei (Dieva Jērs)'
    return render_template('tematiskaissadalijums/SvetasMisesdalas/AgnusDeiDievaJers.html')







if __name__ == '__main__':
    app.run(debug=True , port=5667)