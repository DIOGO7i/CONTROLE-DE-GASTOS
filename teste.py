import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="afram.dev", page_icon="💰")

st.markdown("""
    <div style='background-color: #4ECDC4; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0;'>afram.dev</h1>
        <p style='color: white; margin: 0;'>Controle de Gastos Mensais</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

renda = st.number_input("Qual sua renda mensal?", min_value=0.0)

st.subheader("Seus gastos")
st.caption("💡 Dica: clique duas vezes no campo antes de digitar, pra substituir o valor.")

col1, col2 = st.columns(2)

with col1:
    alimentacao = st.number_input("Alimentação", min_value=0.0)
    transporte = st.number_input("Transporte", min_value=0.0)

with col2:
    cuidados_pessoais = st.number_input("Cuidados pessoais", min_value=0.0)
    assinaturas = st.number_input("Assinaturas", min_value=0.0)

gastos = {
    "alimentação": alimentacao,
    "transporte": transporte,
    "cuidados pessoais": cuidados_pessoais,
    "assinaturas": assinaturas,
}

total_gasto = sum(gastos.values())
saldo = renda - total_gasto

st.divider()
st.subheader("Resumo")

col3, col4 = st.columns(2)

with col3:
    st.metric("Total Gasto", f"R$ {total_gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col4:
    st.metric("Saldo", f"R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
              delta=f"{'Sobrou' if saldo >= 0 else 'Déficit'}")

if total_gasto > 0:
    st.divider()
    st.subheader("Gastos por categoria")
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric("Alimentação", f"R$ {alimentacao:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col6:
        st.metric("Transporte", f"R$ {transporte:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col7:
        st.metric("Cuidados pessoais", f"R$ {cuidados_pessoais:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col8:
        st.metric("Assinaturas", f"R$ {assinaturas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    st.divider()
    st.subheader("Distribuição dos gastos")

    categorias = list(gastos.keys())
    valores = list(gastos.values())
    cores = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#95E1D3"]
    explode = [0, 0, 0, 0.1]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=categorias, autopct='%1.1f%%', colors=cores, explode=explode)
    ax.axis('equal')
    st.pyplot(fig)