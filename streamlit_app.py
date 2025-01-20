import streamlit as st

# _chets_lsit = st.secrets['valor_ref']

_chets_lsit = [1,2]

def getNextChestName(index):
    if _chets_lsit[index] == 0:
        return "Common"
    elif _chets_lsit[index] == 1:
        return "Rare"
    elif _chets_lsit[index] == 2:
        return "Epic"
    else:
        return  "Error! :c"

def getNextIndex(batalha):
    valor_ref = 3484
    index_ref = 42
    
    if batalha >= valor_ref:
        index = index_ref + (batalha % valor_ref)
    else:
        index = index_ref - (valor_ref - batalha)

    index = (index + 1) % 60  # Incrementa o índice e aplica o limite 0-59
    return index


st.title("SQUAD BUSTERS - MY NEXT CHEST!")
st.write(
    "Use seus multiplicadores de baú com mais sabedoria!"
)
st.write(
    "Use your chest multipliers more wisely!"
)
st.write(_chets_lsit)