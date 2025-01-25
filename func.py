import streamlit as st
_chetslist = st.secrets.chest.sequence

# _chets_lsit = [1,2]

def getNextChestNameByIndex(index) -> str:
    if _chetslist[index] == 0:
        return "Common"
    elif _chetslist[index] == 1:
        return "Rare"
    elif _chetslist[index] == 2:
        return "Epic"
    else:
        return  "Ops! Error."


def getNextChestNameByBattle(batalha) -> str:
    return getNextChestNameByIndex(getNextIndex(batalha))


def getNextIndex(batalha) -> int:
    valor_ref = 3484
    index_ref = 42
    
    if batalha >= valor_ref:
        index = index_ref + (batalha % valor_ref)
    else:
        index = index_ref - (valor_ref - batalha)

    index = (index + 1) % 60
    return index


def getHTMLFooter() -> str:
        footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        © 2025 Squad Buster - Next Chets v0.1 - @jvsilvictor.
    </div>
    """
        return footer


def getHTMLChestTable() -> str:
    # URLs ou caminhos das imagens
    image_urls = [
        ["https://via.placeholder.com/100", "https://via.placeholder.com/100"],
        ["https://via.placeholder.com/100", "https://via.placeholder.com/100"],
        ["https://via.placeholder.com/100", "https://via.placeholder.com/100"],
    ]

    # Construção da tabela com HTML
    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    for row in image_urls:
        table_html += "<tr>"
        for img in row:
            table_html += f"""
                <td style='border: 1px solid black; text-align: center;'>
                    <img src='{img}' width='100' height='100'>
                </td>
            """
        table_html += "</tr>"
    table_html += "</table>"

    return table_html