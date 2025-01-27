import streamlit as st

st.image("HARMONIES_LOGO.png")
st.title("Harmonies Score Calculator")

num_players = st.number_input("Number of Players", min_value=1, step=1, max_value=4)
info = {
    "Trees": "#929626",
    "Mountains": "#878886",
    "Fields": "#D7A704",
    "Buildings": "#BA3145",
    "Water": "#007A86"
}

# Layout for player scores
cols = st.columns(num_players)
player_scores = {}
bonuses = {f"Player {idx + 1}": 0 for idx in range(num_players)}  # Initialize bonuses to 0

for idx, col in enumerate(cols):
    with col:
        st.subheader(f"Player {idx + 1}")
        scores = {}
        for token, hex_code in info.items():
            st.markdown(
                f'<div style="background-color:{hex_code}; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; color: white;">{token}</div>',
                unsafe_allow_html=True,
            )
            scores[token] = st.number_input(f"{token} Score",min_value=0, step=1, key=f"{token}_{idx}")
        player_scores[f"Player {idx + 1}"] = scores
        st.markdown(f"**Player {idx + 1} Animal Scores**")
        for i in range(6):
            bonus = st.number_input(f"Score {i + 1}", min_value=0, step=1, key=f"bonus{i}_{idx}")
            bonuses[f"Player {idx + 1}"] += bonus
        

# Calculate total scores
st.subheader("🏆 Final Scores")
score_cols = st.columns(num_players)

final_scores = {}
for idx, col in enumerate(score_cols):
    total_score = sum(player_scores[f"Player {idx + 1}"].values()) + bonuses[f"Player {idx + 1}"]
    final_scores[f"Player {idx + 1}"] = total_score

# Determine the highest score
max_score = max(final_scores.values())
winners = [player for player, score in final_scores.items() if score == max_score]

# Display final scores with winner highlight
for idx, col in enumerate(score_cols):
    with col:
        player = f"Player {idx + 1}"
        if final_scores[player] == max_score:
            st.markdown(
                f'<div style="color: #FFBF00; font-weight: bold; font-size: 24px;">🏅 {player}: {final_scores[player]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(f"**{player}:** {final_scores[player]}")
