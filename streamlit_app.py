import streamlit as st
import func as f


def main():
    st.title("SQUAD BUSTERS - NEXT CHEST!")

    st.write(
        "Use your chest multipliers wisely!"
    )

    st.write("")
    st.write("")
    st.write("")

    # LAYOUT - COLUNAS
    col_e, col_d = st.columns([1, 2])

    with col_e:
        battle_number = st.number_input("Battle Number", key="input_battle", min_value=1, step=1)

    with col_d:
        st.text_area("Texto", height=100)

    st.write(f.getNextChestNameByBattle(battle_number))
    st.write(battle_number)



    # Footer
    st.markdown(f.getFooter(), unsafe_allow_html=True)
if __name__ == "__main__":
    main()