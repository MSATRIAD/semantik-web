import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = "http://localhost:7200/repositories/semantikweb1"  

def run_query(query):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def get_all_lines():
    query = """
    PREFIX ont: <http://contoh.org/ontology#>

    SELECT ?baris ?transliterasi ?terjemahan WHERE {
      ?baris a ont:BarisNaskah ;
             ont:hasTransliteration ?tl ;
             ont:hasTranslation ?tr .
      ?tl ont:value ?transliterasi .
      ?tr ont:value ?terjemahan .
    }
    ORDER BY ?baris
    """
    return run_query(query)

def search_lines(keyword):
    query = f"""
    PREFIX ont: <http://contoh.org/ontology#>

    SELECT ?baris ?transliterasi ?terjemahan WHERE {{
        ?baris a ont:BarisNaskah ;
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
    return run_query(query)


# Streamlit UI
st.title("📜 Naskah Digital: Transliterasi & Terjemahan")

menu = ["Semua Baris", "Pencarian"]
choice = st.sidebar.radio("Menu", menu)

if choice == "Semua Baris":
    st.subheader("📖 Semua Baris Naskah")
    results = get_all_lines()
    for res in results["results"]["bindings"]:
        st.markdown(f"**ID:** {res['baris']['value']}")
        st.markdown(f"📝 *Transliterasi:* {res['transliterasi']['value']}")
        st.markdown(f"📘 *Terjemahan:* {res['terjemahan']['value']}")
        st.markdown("---")

elif choice == "Pencarian":
    st.subheader("🔍 Pencarian Transliterasi")
    keyword = st.text_input("Masukkan kata kunci:")
    if keyword:
        results = search_lines(keyword)
        if results["results"]["bindings"]:
            for res in results["results"]["bindings"]:
                st.markdown(f"**ID:** {res['baris']['value']}")
                st.markdown(f"📝 *Transliterasi:* {res['transliterasi']['value']}")
                st.markdown(f"📘 *Terjemahan:* {res['terjemahan']['value']}")
                st.markdown("---")
        else:
            st.info("Tidak ditemukan hasil.")

