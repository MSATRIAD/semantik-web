import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = "http://localhost:7200/repositories/semantikweb1"  

# Styling aplikasi
st.markdown("""
<style>
[data-testid="stMain"] {
    background-image: url("https://img.freepik.com/free-vector/elegant-golden-irregular-organic-seamless-pattern_1409-4322.jpg?semt=ais_hybrid&w=740");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    position: relative;
    min-height: 100vh;
    width: 100%;
}
[data-testid="stMain"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 0;
    pointer-events: none;
}
h1, h2, h3, p {
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

# Fungsi SPARQL
def run_query(query):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def get_all_lines_grouped():
    query = """
    PREFIX ont: <http://contoh.org/ontology#>

    SELECT ?baris ?transliterasi ?terjemahan WHERE {
      ?baris a ont:SisiHalaman ;
             ont:hasTransliteration ?tl ;
             ont:hasTranslation ?tr .
      ?tl ont:value ?transliterasi .
      ?tr ont:value ?terjemahan .
    }
    ORDER BY ?baris
    """
    result = run_query(query)
    recto = []
    verso = []
    for res in result["results"]["bindings"]:
        uri = res["baris"]["value"]
        entry = {
            "id": uri,
            "transliterasi": res["transliterasi"]["value"],
            "terjemahan": res["terjemahan"]["value"]
        }
        if "recto" in uri:
            recto.append(entry)
        elif "verso" in uri:
            verso.append(entry)
    return recto, verso

def search_lines_grouped(keyword):
    query = f"""
    PREFIX ont: <http://contoh.org/ontology#>

    SELECT ?baris ?transliterasi ?terjemahan WHERE {{
        ?baris a ont:SisiHalaman ;
                ont:hasTransliteration ?tl ;
                ont:hasTranslation ?tr .
        ?tl ont:value ?transliterasi .
        ?tr ont:value ?terjemahan .

        FILTER (
            CONTAINS(LCASE(STR(?transliterasi)), LCASE("{keyword}")) ||
            CONTAINS(LCASE(STR(?terjemahan)), LCASE("{keyword}"))
        )
    }}
    ORDER BY ?baris
    """
    result = run_query(query)
    recto = []
    verso = []
    for res in result["results"]["bindings"]:
        uri = res["baris"]["value"]
        entry = {
            "id": uri,
            "transliterasi": res["transliterasi"]["value"],
            "terjemahan": res["terjemahan"]["value"]
        }
        if "recto" in uri:
            recto.append(entry)
        elif "verso" in uri:
            verso.append(entry)
    return recto, verso


def get_total_triples():
    query = "SELECT (COUNT(*) AS ?total) WHERE { ?s ?p ?o }"
    result = run_query(query)
    return int(result["results"]["bindings"][0]["total"]["value"])

def get_total_by_posisi(posisi):
    query = f"""
    PREFIX ont: <http://contoh.org/ontology#>
    SELECT (COUNT(?baris) AS ?jumlah) WHERE {{
      ?baris a ont:BarisNaskah ;
             ont:hasPosisi "{posisi}" .
    }}
    """
    result = run_query(query)
    return int(result["results"]["bindings"][0]["jumlah"]["value"])

# Sidebar
st.sidebar.title("Website Translasi Sanghyang Tatwa Ajnyana")
st.sidebar.markdown("---")
st.sidebar.write("""
Aplikasi ini dirancang untuk membantu dalam memahami naskah Sanghyang Tatwa Ajnyana  
*[Dokumen Sanghyang Tatwa Ajnyana](https://www.academia.edu/5937886/_With_Tien_Wartini_et_al_2011_Sanghyang_Tatwa_Ajnyana_Teks_dan_Terjemahan#loswp-work-container)*
""")

# Informasi dataset
total_triples = get_total_triples()

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Statistik Tripel")
st.sidebar.markdown(f"- Total triples: *{total_triples}*")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 Panduan Pencarian")
st.sidebar.markdown("""
- Masukkan kata atau frasa dari transliterasi atau terjemahan.
- Pencarian tidak peka huruf kapital.
- Contoh: dewa, roh, hyang
""")

# Tampilan utama
st.title("📜 Naskah Digital: Transliterasi & Terjemahan")

tab1, tab2 = st.tabs(["📖 Semua Baris", "🔍 Pencarian"])

with tab1:
    st.subheader("📖 Semua Baris Naskah")
    recto, verso = get_all_lines_grouped()

    with st.expander("📄 Recto"):
        for res in recto:
            st.markdown(f"*URI:* {res['id']}")
            st.markdown(f"📝 Transliterasi: {res['transliterasi']}")
            st.markdown(f"📘 Terjemahan: {res['terjemahan']}")
            st.markdown("---")

    with st.expander("📄 Verso"):
        for res in verso:
            st.markdown(f"*ID:* {res['id']}")
            st.markdown(f"📝 Transliterasi: {res['transliterasi']}")
            st.markdown(f"📘 Terjemahan: {res['terjemahan']}")
            st.markdown("---")


with tab2:
    st.subheader("🔍 Pencarian Transliterasi atau Terjemahan")
    keyword = st.text_input("Masukkan kata kunci:")
    if keyword:
        recto, verso = search_lines_grouped(keyword)

        if not recto and not verso:
            st.info("Tidak ditemukan hasil.")

        if recto:
            with st.expander("📄 Recto"):
                for res in recto:
                    st.markdown(f"*ID:* {res['id']}")
                    st.markdown(f"📝 Transliterasi: {res['transliterasi']}")
                    st.markdown(f"📘 Terjemahan: {res['terjemahan']}")
                    st.markdown("---")

        if verso:
            with st.expander("📄 Verso"):
                for res in verso:
                    st.markdown(f"*ID:* {res['id']}")
                    st.markdown(f"📝 Transliterasi: {res['transliterasi']}")
                    st.markdown(f"📘 Terjemahan: {res['terjemahan']}")
                    st.markdown("---")
